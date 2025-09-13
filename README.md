# 📰 AI News Summarizer & Q&A Tool  

A beginner-friendly Python project that:  

- 📄 **Summarizes any news article** in 3–4 sentences  
- ❓ **Lets you ask questions** about the article (Q&A mode)  
- 🎛 **Experiments with creativity levels** (temperature = 0.1 / 0.7 / 1.0)  
- 📂 **Logs all results** to help with your analysis & write-up  

Built as part of **Week 4 of the AI Fellowship** — powered by **Gemini API (Google AI Studio)**.

---

## ✨ Features

✅ Paste or load any article text (.txt or stdin)  
✅ Shows **article length** (words + characters)  
✅ Generates a **clear, concise 3–4 sentence summary**  
✅ Supports **interactive Q&A** — answers based only on the article  
✅ Creates **multiple summaries at different temperatures**  

| Temperature | Style                          |
|-------------|--------------------------------|
| `0.1`       | Robotic, factual, deterministic |
| `0.7`       | Balanced, natural (recommended) |
| `1.0`       | Creative, free-flowing          |

🗂 **Auto-saves results** in `runs/` for easy analysis.

---

## 📁 Project Structure

```

AI-NEWS-SUMMARIZER/
│── summarizer.py      # Main script
│── requirements.txt   # Dependencies
│── article.txt        # Paste your article here
│── observations.md    # Your notes on temperature outputs
│── rubric.md          # (Optional) Scoring rubric
│── runs/              # Auto-saved summaries & outputs
└── .env               # Contains GEMINI\_API\_KEY (keep this private!)

````

⚠ **Important:** Add `.env` and `runs/*.json` to `.gitignore` before pushing to GitHub.

---

## ⚙ Setup Instructions

1. **Install Python** (3.10+ recommended):  
   ```bash
   python --version
````

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

   * **Windows:**

     ```bash
     .venv\Scripts\activate
     ```
   * **macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Gemini API Key**

   * Get a key from [Google AI Studio](https://aistudio.google.com/).
   * Create a `.env` file in the root:

     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

---

## ▶ How to Use

### Option 1 — From a `.txt` File (Recommended)

```bash
python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0" --qa
```

### Option 2 — Paste Text in Terminal

```bash
python summarizer.py --stdin --experiment-temps "0.1,0.7,1.0" --qa
```

### Option 3 — From a URL (if supported)

```bash
python summarizer.py --url "https://example.com/article" --experiment-temps "0.1,0.7,1.0" --qa
```

⚠ Many websites block scraping. If you get 401/403 errors, copy-paste the article into `article.txt` instead.

---

## 💬 Q\&A Mode

After summarization, the script will let you ask questions:

```text
Q1: Who performed at Wembley Stadium?
Q2: How many people attended their tour?
Q3: What was unique about their concert?
```

Answers will use only the article text (not external knowledge).

---

## 📊 Temperature Experiments

Compare summaries at different **creativity levels**:

* `0.1` → strict, factual
* `0.7` → natural, recommended
* `1.0` → creative, free-flowing

You can copy these results to `observations.md` for your assignment.

---

## 📌 .gitignore

Add the following to keep sensitive files safe:

```
.env
.venv/
__pycache__/
*.pyc
runs/*.json
```

---

## 🧠 Notes

* Designed for **beginners learning LLM workflows**
* Runs **locally** — no external servers needed
* Great practice for experimenting with **prompting & temperature tuning**
* Perfect for **Fellowship assignments or personal learning**

---
\
