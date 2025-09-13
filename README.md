📰 AI News Summarizer & Q&A Tool
A beginner-friendly Python tool that:

Summarizes any news article in 3–4 clear sentences
Lets you ask at least 3 questions about the article
Tests how summaries change at different creativity levels (temperature 0.1 / 0.7 / 1.0)
Logs your results and analysis for your assignment
Built as part of Week 4 of the AI Fellowship, using the Gemini API by Google.

✨ Features
Input any article (paste text, use a .txt file, or URL if supported)

Shows original article length (words + characters)

Generates a concise summary (3–4 sentences)

Allows interactive Q&A based only on the article

Creates multiple summaries at different temperatures

0.1 → Robotic & factual
0.7 → Balanced & clear
1.0 → More creative & free
Saves all outputs in the runs/ folder for analysis

Helps you complete observations.md for your assignment write-up

📁 Project Structure
AI-NEWS-SUMMARIZER/
│── summarizer.py      # Main script
│── requirements.txt   # Dependencies
│── article.txt        # Paste your article here
│── observations.md    # Analysis of temperature outputs
│── rubric.md          # (Optional) Quality scoring rubric
│── runs/              # Auto-saved summaries & experiment outputs
└── .env               # Contains GEMINI_API_KEY (keep private!)
⚠ Important: .env must not be pushed to GitHub. Add it to .gitignore.

⚙ Setup Instructions
1. Install Python
Make sure you have Python 3.10+ installed:

python --version
2. Create a Virtual Environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Add Your Gemini API Key
Get a key from Google AI Studio.
Create a .env file in the project root with:
GEMINI_API_KEY=your_api_key_here
▶ How to Use
Option 1 — From a .txt File (Recommended)
Paste your article into article.txt and run:

python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0" --qa
Option 2 — Paste Text in Terminal
python summarizer.py --stdin --experiment-temps "0.1,0.7,1.0" --qa
Option 3 — From a URL (if supported)
python summarizer.py --url "https://example.com/article" --experiment-temps "0.1,0.7,1.0" --qa
⚠ Many sites block scraping. If you see 403 or 401 errors, copy the article into article.txt instead.

💬 Asking Questions (Q&A)
After summarization, the script will ask you to enter questions. Example:

Q1: Who performed at Wembley Stadium?
Q2: How many people attended their tour?
Q3: What was unique about their concert?
The tool answers using only the article text.

📊 Temperature Experiments
You can compare how summaries change at different temperatures:

0.1 → Robotic, factual
0.7 → Balanced, natural
1.0 → Creative, free-flowing
All results are auto-saved into runs/ and can be copied into observations.md for your analysis.

📌 .gitignore
Make sure your .gitignore includes:

.env
.venv/
_pycache_/
*.pyc
runs/*.json
📎 Notes
Designed for learning & practice with LLMs in real-world tasks
Beginner-friendly — requires only basic Python
All work runs locally on your machine