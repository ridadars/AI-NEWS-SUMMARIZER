# 📰 AI News Summarizer & Q&A (Week 4 Assignment)

This project is a Python-based **AI News Summarizer and Q&A Tool** built using the [Gemini API](https://aistudio.google.com/) by [Google](https://about.google/).  
It was created as part of my Week 4 assignment for the AI Fellowship.

---

## 📌 Features

- Summarizes any news article into **3–4 sentences**
- Shows **original article length** (word and character count)
- Lets the user ask **at least 3 questions about the article**
- Supports **different temperature settings** (0.1, 0.7, 1.0) to compare output styles
- Optional **fun summary styles** (`pirate`, `comedian`, `sports`)
- Saves summaries and experiment results inside a `runs/` folder

---

## 📁 Project Structure

ai-news-summarizer/
│
├── summarizer.py # Main script
├── requirements.txt # Python dependencies
├── article.txt # Paste your article text here
├── observations.md # Record your temperature experiment results
├── rubric.md # Optional scoring rubric for evaluation
├── .env # Your Gemini API key (DO NOT upload to GitHub)
└── runs/ # Generated outputs (summaries, JSON files)

---

## ⚙️ Setup Instructions

### 1) Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-news-summarizer.git
cd ai-news-summarizer
2) Create a Virtual Environment (optional but recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
3) Install the Requirements
pip install -r requirements.txt
4) Add Your Gemini API Key
Get your API key from Google AI Studio

Create a .env file in the project folder and add:
GEMINI_API_KEY=your_api_key_here
▶️ Usage
A) Using a .txt File (recommended)
Paste your article content into article.txt and run:
python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0" --qa
B) Pasting Text Directly
python summarizer.py --stdin --experiment-temps "0.1,0.7,1.0" --qa
C) Using an Article URL (if the site allows scraping)
python summarizer.py --url "https://www.techcrunch.com/some-article" --experiment-temps "0.1,0.7,1.0" --qa
💬 Interactive Q&A
After the summary is printed, the script will ask:
Q1:
Q2:
Q3:
Type at least 3 questions related to the article, and the model will answer them using the article text as context.