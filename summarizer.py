import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types as genai_types

RUNS_DIR = Path("./runs")
RUNS_DIR.mkdir(exist_ok=True)

def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def extract_text_from_url(url: str) -> str:
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "aside", "footer", "noscript", "form"]):
        tag.decompose()
    candidates = soup.select("article") or soup.select("main") or []
    paragraphs: List[str] = []
    def grab_paras(node):
        for p in node.find_all("p"):
            txt = p.get_text(separator=" ", strip=True)
            if txt and len(txt.split()) > 3:
                paragraphs.append(txt)
    if candidates:
        for c in candidates:
            grab_paras(c)
    else:
        grab_paras(soup)
    return clean_text("\n".join(paragraphs))

def read_text_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return clean_text(f.read())

def read_text_from_stdin() -> str:
    print("Paste your article text below. Press ENTER twice (blank line) to finish:\n", file=sys.stderr)
    lines = []
    blank = False
    for line in sys.stdin:
        if line.strip() == "":
            blank = True
            break
        lines.append(line)
    return clean_text("".join(lines))

def count_words_chars(text: str) -> Dict[str, int]:
    return {"words": len(text.split()), "chars": len(text)}

@dataclass
class ModelConfig:
    model: str = "gemini-2.5-flash"
    temperature: float = 0.7
    disable_thinking: bool = False
    style: Optional[str] = None

def build_summary_prompt(article_text: str, style: Optional[str]) -> str:
    base = (
        "You are an expert news assistant. Summarize the following article in 3–4 sentences. "
        "Stay faithful to the source, avoid speculation, and include the core who/what/when/why. "
        "If the article is opinion or analysis, make that explicit in the summary.\n\n"
        f"Article:\n{article_text}\n\n"
    )
    if style:
        style_map = {
            "pirate": "Rewrite the summary in the playful style of a pirate.",
            "comedian": "Rewrite the summary in a light, witty comedic tone.",
            "sports": "Rewrite the summary as a brief sports commentary.",
        }
        base += style_map.get(style.lower(), "")
    return base

def build_qa_prompt(article_text: str, question: str) -> str:
    return (
        "Answer the question using ONLY the article text. "
        "If the article does not contain the answer, say 'Not stated in the article.' "
        "Be concise (2–4 sentences).\n\n"
        f"Question: {question}\n"
        f"Article: {article_text}\n"
    )

def call_gemini(prompt: str, cfg: ModelConfig) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment or .env")
    client = genai.Client(api_key=api_key)
    thinking_cfg = genai_types.ThinkingConfig(thinking_budget=0) if cfg.disable_thinking else None
    gcfg = genai_types.GenerateContentConfig(temperature=cfg.temperature, thinking_config=thinking_cfg)
    resp = client.models.generate_content(model=cfg.model, contents=prompt, config=gcfg)
    return resp.text or ""

def main():
    parser = argparse.ArgumentParser(description="AI News Summarizer & Q&A Tool (Gemini-only)")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash")
    src = parser.add_mutually_exclusive_group(required=False)
    src.add_argument("--url", type=str, help="Article URL to fetch")
    src.add_argument("--file", type=str, help="Path to a local .txt file containing the article")
    src.add_argument("--stdin", action="store_true", help="Paste article text into stdin")
    parser.add_argument("--style", choices=["pirate", "comedian", "sports"])
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--disable-thinking", action="store_true")
    parser.add_argument("--experiment-temps", type=str, default="")
    parser.add_argument("--qa", action="store_true")
    parser.add_argument("--max-questions", type=int, default=3)
    args = parser.parse_args()

    if args.url:
        article_text = extract_text_from_url(args.url)
    elif args.file:
        article_text = read_text_from_file(args.file)
    elif args.stdin:
        article_text = read_text_from_stdin()
    else:
        parser.error("Please provide one of --url, --file, or --stdin")

    stats = count_words_chars(article_text)
    print("\n" + "="*80)
    print("Original article length:", f"{stats['words']} words,", f"{stats['chars']} characters")
    print("="*80 + "\n")

    cfg = ModelConfig(model=args.model, temperature=args.temperature, disable_thinking=args.disable_thinking, style=args.style)

    prompt = build_summary_prompt(article_text, cfg.style)
    print(f"[Summary @ temp={cfg.temperature}]")
    summary = call_gemini(prompt, cfg)
    print(summary.strip(), "\n")

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    (RUNS_DIR / f"summary_{timestamp}.txt").write_text(summary, encoding="utf-8")

    if args.experiment_temps:
        temps = [float(t.strip()) for t in args.experiment_temps.split(",") if t.strip()]
        results = []
        for t in temps:
            cfg.temperature = t
            out = call_gemini(build_summary_prompt(article_text, cfg.style), cfg).strip()
            results.append({"temperature": t, "summary": out})
            print(f"\n[Experiment Summary @ temp={t}]\n{out}\n")
        with open(RUNS_DIR / f"experiments_{timestamp}.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

    if args.qa:
        print("\n" + "="*80)
        print("Interactive Q&A")
        print("="*80)
        for i in range(1, args.max_questions + 1):
            q = input(f"Q{i}: ").strip()
            if not q:
                continue
            ans = call_gemini(build_qa_prompt(article_text, q), cfg)
            print(f"A{i}: {ans.strip()}\n")

if __name__ == "__main__":
    main()
