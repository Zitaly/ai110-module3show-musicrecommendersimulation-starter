# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world platforms utilize a pipeline approach that first pulls a select number of candidates, ranks them using a deeper model, adjusts the rankings, and saves new data for further training. For this content-based system, the prioritized features, which are in the order of energy, mood, acousticness, genre, and valence, with weights of 3.0, 2.5, 2.0, 1.5, and 1.0 respectively, produce sub-scores between 0 and 1 that are multiplied by their weights. These are then added up to create the score, which has a max of 10. Mood only works if the song's mood equals the user's favorite mood. Acousticness only works if the user likes acousticness. Otherwise, it subtracts. Genre only works when the song's genre matches the user's favorite genre. 


The user's profile will track each feature and whether the user has a preference, and the songs will track the features for that particular song. The user, for example, when choosing valence, could have a scale showing what songs are at what valence.

User:
favorite_genre: str
favorite_mood: str
target_energy: float
likes_acoustic: bool
target_valence: float

Song:
id: int
title: str
artist: str
genre: str
mood: str
energy: float
tempo_bpm: float
valence: float
danceability: float
acousticness: float

The system will first take in the user's preferences. After that, it will apply the above scoring system to each song and compare it to the user's preferences. After that, the top 5 songs will be shown. If a user prefers the categories with lower weights, they may see less songs that they like. There's a bias toward energy.

Perhaps the user can ask to see more recommendations.
---
## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



