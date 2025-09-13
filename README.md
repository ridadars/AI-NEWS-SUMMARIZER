# 📰 AI News Summarizer & Q&A (Gemini API)

**Week 4 Fellowship Assignment** — a beginner-friendly Python tool that:
- Summarizes any news article in **3–4 sentences**
- Lets you ask **at least 3 questions** about that article
- Compares model behavior at **temperatures 0.1 / 0.7 / 1.0**
- Saves run outputs in a `runs/` folder
- (Bonus) Fun styles: `pirate`, `comedian`, `sports`

Built with the [Gemini API](https://aistudio.google.com/) by Google.

---

## ✨ Features
- **Summarization:** short, faithful summaries (3–4 sentences)
- **Interactive Q&A:** ask questions based on the article only
- **Experiments:** test temperatures and record observations
- **Input options:** URL (if allowed), local `.txt`, or paste via stdin
- **Safe prompts:** Q&A answers “Only from the article; otherwise say ‘Not stated in the article.’”

---

## 📁 Project Structure
ai-news-summarizer/
├── summarizer.py # Main script
├── requirements.txt # Dependencies
├── article.txt # Paste your article text here
├── observations.md # Fill in your temperature findings
├── rubric.md # (Optional) Quality scoring table
├── runs/ # Generated summaries & experiment JSONs
└── .env # GEMINI_API_KEY=... (DO NOT COMMIT)

yaml
Copy code

> ⚠️ Add `.env` and `.venv/` to `.gitignore` so your key & venv aren’t uploaded.

---

## ⚙️ Setup

1) **Python 3.10+**  
   ```bash
   python --version
(Recommended) Virtual environment

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Gemini API key

Get one from Google AI Studio → https://aistudio.google.com/

Create a file named .env in the project folder:

ini
Copy code
GEMINI_API_KEY=your_api_key_here
▶️ Usage
Option A — Use a .txt file (recommended)
Put your article in article.txt, then:

bash
Copy code
python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0" --qa
Option B — Paste text in terminal
bash
Copy code
python summarizer.py --stdin --experiment-temps "0.1,0.7,1.0" --qa
You’ll be prompted: “Paste your article text…”

Option C — Use a URL (not all sites allow scraping)
bash
Copy code
python summarizer.py --url "https://example.com/your-article" --experiment-temps "0.1,0.7,1.0" --qa
If the site blocks scraping (e.g., many BBC/Reuters pages), copy/paste the text into article.txt instead.

💬 Q&A Prompting (what the script sends)
Each question is sent along with the full article text, e.g.:

vbnet
Copy code
Question: [your question]
Article: [full article text]
The model is instructed to answer only using the article.

🧪 Record Your Observations
Run:

bash
Copy code
python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0"
Open observations.md and paste the 3 summaries (0.1 / 0.7 / 1.0).

Write what changed, which temperature was best, and why.

🔧 Useful Flags
--style pirate|comedian|sports → fun summary tone

--disable-thinking → reduces reasoning budget (faster/cheaper on 2.5-flash)

--max-questions 5 → ask more than three questions

🧯 Troubleshooting
401/403 on URL input: the site likely blocks scraping → use --file or --stdin.

Key not found: ensure .env exists and contains GEMINI_API_KEY=....

Accidentally committed .env:

git rm --cached .env

Add .env to .gitignore

Commit & push; rotate the key in AI Studio.

🛡️ Privacy
Never commit .env (API keys) or your .venv/ folder. Recommended .gitignore:

markdown
Copy code
.env
.venv/
__pycache__/
*.pyc
runs/*.json
