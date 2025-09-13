# 📰 AI News Summarizer & Q&A Tool

A simple and beginner-friendly Python tool that:
- Summarizes any news article in **3–4 clear sentences**
- Lets you ask **at least 3 questions** about the article
- Tests how summaries change at **different creativity levels (temperature 0.1 / 0.7 / 1.0)**
- Logs your results and analysis for your assignment

This project was built as part of **Week 4 of the AI Fellowship**, using the [Gemini API](https://aistudio.google.com/) by [Google](https://about.google/).

---

## ✨ What It Does
This tool makes it easier to work with long articles.  
You give it an article (by pasting it or using a `.txt` file), and it:

1. Shows the **original article length** in words and characters  
2. Creates a **3–4 sentence summary**  
3. Lets you **ask questions** about the article content  
4. Generates **multiple summaries at different temperatures (0.1 = robotic, 1.0 = creative)**  
5. Helps you **record your observations** and complete your assignment write-up

---

## 📁 Project Structure

AI-NEWS-SUMMARIZER/
│
├── summarizer.py # Main script
├── requirements.txt # All dependencies
├── article.txt # Paste your article here
├── observations.md # Your analysis of temperature outputs
├── rubric.md # (Optional) Quality scoring rubric
├── runs/ # Auto-saved summaries and experiment outputs
└── .env # Contains GEMINI_API_KEY (keep this private!)

go
Copy code

> ⚠️ `.env` must **not** be pushed to GitHub — make sure it’s in your `.gitignore`

## ⚙️ Setup Instructions

### 1. Install Python
Make sure you have Python 3.10+ installed:
```bash
python --version
2. Create a Virtual Environment
This keeps your project clean and separate.

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Add Your Gemini API Key
Get a key from Google AI Studio

Create a file called .env in the project folder with this inside:

env
Copy code
GEMINI_API_KEY=your_api_key_here
▶️ How to Use
Option 1 — Use a .txt File (recommended)
Paste your article into article.txt and run:

bash
Copy code
python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0" --qa
Option 2 — Paste Text in Terminal
bash
Copy code
python summarizer.py --stdin --experiment-temps "0.1,0.7,1.0" --qa
Option 3 — Use a URL (if allowed)
bash
Copy code
python summarizer.py --url "https://example.com/article" --experiment-temps "0.1,0.7,1.0" --qa
⚠️ Many sites block scraping. If you get a 403 or 401 error, copy the article into article.txt instead.

💬 Asking Questions (Q&A)
After summarization, the script will ask you to enter questions like:

makefile
Copy code
Q1: Who performed at Wembley Stadium?
Q2: How many people attended their tour?
Q3: What was unique about their concert?
Each question is answered using only the article text.

📊 Temperature Experiments
You can test how creativity affects summaries:

0.1 → Robotic, factual

0.7 → Balanced and clear

1.0 → More creative and free

All outputs are saved into runs/, and you can paste them into observations.md to write your comparison.

📌 .gitignore (important!)
Make sure these are inside your .gitignore so they don’t get uploaded:

markdown
Copy code
.env
.venv/
__pycache__/
*.pyc
runs/*.json
📎 Notes
This project is designed for learning how to use LLMs (Large Language Models) in real-world tasks.

It’s intentionally beginner-friendly — you only need basic Python to run it.

All work stays local on your machine.