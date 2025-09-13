# Observations on Temperature Experiments (Gemini)

> Ran: `python summarizer.py --file article.txt --experiment-temps "0.1,0.7,1.0"`

## Article
- Title/URL: https://www.bbc.com/news/articles/c306m86y824o
- Model: gemini-2.5-flash
- Article length (words / chars): 1202 / 7017 


## Side-by-side Summaries
### Temp = 0.1 (deterministic/robotic)
This article offers an analysis of Coldplay's final, dazzling concert at Wembley Stadium, which concluded their record-breaking 10-show run as part 
of their "Music Of The Spheres Tour." The show, postponed due to a transport strike, was described as a sensory-overload experience prioritizing 
audience unity through LED wristbands, immersive visuals, and Chris Martin's engaging performance. The tour has become the highest-attended in history,
with over 13 million tickets sold, and is set to resume in southern Africa in about 18 months. The review highlights the band's unique stadium stagecraft and the communal euphoria it fosters among fans.


### Temp = 0.7 (balanced)
Coldplay concluded their record-breaking 10-show run at Wembley Stadium, part of their "Music Of The Spheres" Tour, with a dazzling, multi-coloured 
concert experience. This article, a concert review, highlights the band's exceptional stadium stagecraft, Chris Martin's engaging performance, and the unique fan interaction, making the audience an integral part of the show with LED wristbands. The tour, which has sold over 13 million tickets 
globally since 2022, will now go on hiatus before resuming in southern Africa in about 18 months. The review emphasizes the communal euphoria and immersive spectacle that defines Coldplay's live performances, even after the final Wembley date was postponed due to transport strikes.

### Temp = 1.0 (creative)
This article provides an enthusiastic analysis of Coldplay's final concert at Wembley Stadium, which marked the end of their record-breaking 10-show
run and the latest leg of their "Music Of The Spheres Tour" on Friday. It describes the show as "stadium stagecraft at its absolute finest," 
emphasizing the band's unique audience-centric approach through LED wristbands, elaborate visuals, and lead singer Chris Martin's engaging, humorous inter
actions. Despite a postponement due to a transport strike and the band's announced future hiatus from albums, the review asserts that Coldplay's ability to foster a "communal euphoria" guarantees their continued success and fan devotion.


## Analysis

- **How the summaries changed as temperature increased:**
  - **0.1:** The summary was very robotic and plain. It only stated facts and numbers directly from the article without any excitement. It sounded like a list of points rather than a proper paragraph.
  - **0.7:** This version felt much more natural and human. It was still accurate but flowed better, and used nicer words to connect ideas. It gave a clear picture without being too long or dry.
  - **1.0:** The 1.0 version was the most enthusiastic and descriptive. It used more creative wording and made the concert sound exciting, but it was slightly longer and less focused on just the key points.

- **Usefulness:** I think the 0.7 summary was the most useful because it gave a good balance. It was clear and easy to read like a real article summary, but still accurate and not too wordy.

- **Accuracy:** The 0.1 and 0.7 summaries stayed very close to the original text. The 1.0 version also stayed accurate, but added more dramatic tone and slightly exaggerated the excitement, even though it didn’t add false facts.

- **Style/tone notes:**  
  - 0.1 → dry and robotic  
  - 0.7 → clear, balanced, and professional  
  - 1.0 → energetic and fun but a bit long and dramatic

## Final Pick

- **Chosen temperature:** 0.7  
- **Reason:** It gave the most balanced result. It included all the important facts from the article, stayed accurate, and was pleasant to read without sounding too plain or too dramatic. It felt like a real news summary.