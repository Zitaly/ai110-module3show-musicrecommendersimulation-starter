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
Loading songs from data/songs.csv...

================================================================
  High-Energy Pop Fan
  pop | happy | energy 0.85 | non-acoustic | valence 0.80
================================================================

1. Sunrise City - Neon Echo                            9.51 / 10
     - energy 0.82 vs your target 0.85 (+2.91)
     - matches your mood 'happy' (+2.50)
     - acousticness 0.18, you prefer non-acoustic (+1.64)
     - matches your favorite genre 'pop' (+1.50)
     - positivity 0.84 vs your target 0.80 (+0.96)

2. Rooftop Lights - Indigo Parade                      7.52 / 10
     - energy 0.76 vs your target 0.85 (+2.73)
     - matches your mood 'happy' (+2.50)
     - acousticness 0.35, you prefer non-acoustic (+1.30)
     - genre 'indie pop' isn't your 'pop' (+0.00)
     - positivity 0.81 vs your target 0.80 (+0.99)

3. Gym Hero - Max Pulse                                7.13 / 10
     - energy 0.93 vs your target 0.85 (+2.76)
     - mood 'intense' isn't your 'happy' (+0.00)
     - acousticness 0.05, you prefer non-acoustic (+1.90)
     - matches your favorite genre 'pop' (+1.50)
     - positivity 0.77 vs your target 0.80 (+0.97)

4. Neon Skyline Drop - Pulse Theory                    5.57 / 10
     - energy 0.95 vs your target 0.85 (+2.70)
     - mood 'euphoric' isn't your 'happy' (+0.00)
     - acousticness 0.04, you prefer non-acoustic (+1.92)
     - genre 'edm' isn't your 'pop' (+0.00)
     - positivity 0.85 vs your target 0.80 (+0.95)

5. Crown the Block - Verse Kingdom                     5.41 / 10
     - energy 0.78 vs your target 0.85 (+2.79)
     - mood 'confident' isn't your 'happy' (+0.00)
     - acousticness 0.12, you prefer non-acoustic (+1.76)
     - genre 'hip hop' isn't your 'pop' (+0.00)
     - positivity 0.66 vs your target 0.80 (+0.86)


================================================================
  Chill Lofi Studier
  lofi | chill | energy 0.38 | acoustic | valence 0.60
================================================================

1. Library Rain - Paper Lanterns                       9.63 / 10
     - energy 0.35 vs your target 0.38 (+2.91)
     - matches your mood 'chill' (+2.50)
     - acousticness 0.86, you like acoustic (+1.72)
     - matches your favorite genre 'lofi' (+1.50)
     - positivity 0.60 vs your target 0.60 (+1.00)

2. Midnight Coding - LoRoom                            9.26 / 10
     - energy 0.42 vs your target 0.38 (+2.88)
     - matches your mood 'chill' (+2.50)
     - acousticness 0.71, you like acoustic (+1.42)
     - matches your favorite genre 'lofi' (+1.50)
     - positivity 0.56 vs your target 0.60 (+0.96)

3. Spacewalk Thoughts - Orbit Bloom                    7.99 / 10
     - energy 0.28 vs your target 0.38 (+2.70)
     - matches your mood 'chill' (+2.50)
     - acousticness 0.92, you like acoustic (+1.84)
     - genre 'ambient' isn't your 'lofi' (+0.00)
     - positivity 0.65 vs your target 0.60 (+0.95)

4. Focus Flow - LoRoom                                 6.99 / 10
     - energy 0.40 vs your target 0.38 (+2.94)
     - mood 'focused' isn't your 'chill' (+0.00)
     - acousticness 0.78, you like acoustic (+1.56)
     - matches your favorite genre 'lofi' (+1.50)
     - positivity 0.59 vs your target 0.60 (+0.99)

5. Coffee Shop Stories - Slow Stereo                   5.64 / 10
     - energy 0.37 vs your target 0.38 (+2.97)
     - mood 'relaxed' isn't your 'chill' (+0.00)
     - acousticness 0.89, you like acoustic (+1.78)
     - genre 'jazz' isn't your 'lofi' (+0.00)
     - positivity 0.71 vs your target 0.60 (+0.89)


================================================================
  Intense Rock Head
  rock | intense | energy 0.92 | non-acoustic | valence 0.45
================================================================

1. Storm Runner - Voltline                             9.74 / 10
     - energy 0.91 vs your target 0.92 (+2.97)
     - matches your mood 'intense' (+2.50)
     - acousticness 0.10, you prefer non-acoustic (+1.80)
     - matches your favorite genre 'rock' (+1.50)
     - positivity 0.48 vs your target 0.45 (+0.97)

2. Gym Hero - Max Pulse                                8.05 / 10
     - energy 0.93 vs your target 0.92 (+2.97)
     - matches your mood 'intense' (+2.50)
     - acousticness 0.05, you prefer non-acoustic (+1.90)
     - genre 'pop' isn't your 'rock' (+0.00)
     - positivity 0.77 vs your target 0.45 (+0.68)

3. Iron Tempest - Graveforge                           5.64 / 10
     - energy 0.97 vs your target 0.92 (+2.85)
     - mood 'aggressive' isn't your 'intense' (+0.00)
     - acousticness 0.03, you prefer non-acoustic (+1.94)
     - genre 'metal' isn't your 'rock' (+0.00)
     - positivity 0.30 vs your target 0.45 (+0.85)

4. Neon Skyline Drop - Pulse Theory                    5.43 / 10
     - energy 0.95 vs your target 0.92 (+2.91)
     - mood 'euphoric' isn't your 'intense' (+0.00)
     - acousticness 0.04, you prefer non-acoustic (+1.92)
     - genre 'edm' isn't your 'rock' (+0.00)
     - positivity 0.85 vs your target 0.45 (+0.60)

5. Crown the Block - Verse Kingdom                     5.13 / 10
     - energy 0.78 vs your target 0.92 (+2.58)
     - mood 'confident' isn't your 'intense' (+0.00)
     - acousticness 0.12, you prefer non-acoustic (+1.76)
     - genre 'hip hop' isn't your 'rock' (+0.00)
     - positivity 0.66 vs your target 0.45 (+0.79)


================================================================
  Melancholic Classical Listener
  classical | melancholic | energy 0.22 | acoustic | valence 0.20
================================================================

1. Autumn Requiem - Elena Marlowe                      9.93 / 10
     - energy 0.22 vs your target 0.22 (+3.00)
     - matches your mood 'melancholic' (+2.50)
     - acousticness 0.97, you like acoustic (+1.94)
     - matches your favorite genre 'classical' (+1.50)
     - positivity 0.21 vs your target 0.20 (+0.99)

2. Paper Boats - Hollow Pines                          5.51 / 10
     - energy 0.30 vs your target 0.22 (+2.76)
     - mood 'sad' isn't your 'melancholic' (+0.00)
     - acousticness 0.90, you like acoustic (+1.80)
     - genre 'folk' isn't your 'classical' (+0.00)
     - positivity 0.25 vs your target 0.20 (+0.95)

3. Spacewalk Thoughts - Orbit Bloom                    5.21 / 10
     - energy 0.28 vs your target 0.22 (+2.82)
     - mood 'chill' isn't your 'melancholic' (+0.00)
     - acousticness 0.92, you like acoustic (+1.84)
     - genre 'ambient' isn't your 'classical' (+0.00)
     - positivity 0.65 vs your target 0.20 (+0.55)

4. Library Rain - Paper Lanterns                       4.93 / 10
     - energy 0.35 vs your target 0.22 (+2.61)
     - mood 'chill' isn't your 'melancholic' (+0.00)
     - acousticness 0.86, you like acoustic (+1.72)
     - genre 'lofi' isn't your 'classical' (+0.00)
     - positivity 0.60 vs your target 0.20 (+0.60)

5. Coffee Shop Stories - Slow Stereo                   4.82 / 10
     - energy 0.37 vs your target 0.22 (+2.55)
     - mood 'relaxed' isn't your 'melancholic' (+0.00)
     - acousticness 0.89, you like acoustic (+1.78)
     - genre 'jazz' isn't your 'classical' (+0.00)
     - positivity 0.71 vs your target 0.20 (+0.49)


================================================================
  EDM Party Goer
  edm | euphoric | energy 0.95 | non-acoustic | valence 0.85
================================================================

1. Neon Skyline Drop - Pulse Theory                    9.92 / 10
     - energy 0.95 vs your target 0.95 (+3.00)
     - matches your mood 'euphoric' (+2.50)
     - acousticness 0.04, you prefer non-acoustic (+1.92)
     - matches your favorite genre 'edm' (+1.50)
     - positivity 0.85 vs your target 0.85 (+1.00)

2. Gym Hero - Max Pulse                                5.76 / 10
     - energy 0.93 vs your target 0.95 (+2.94)
     - mood 'intense' isn't your 'euphoric' (+0.00)
     - acousticness 0.05, you prefer non-acoustic (+1.90)
     - genre 'pop' isn't your 'edm' (+0.00)
     - positivity 0.77 vs your target 0.85 (+0.92)

3. Iron Tempest - Graveforge                           5.33 / 10
     - energy 0.97 vs your target 0.95 (+2.94)
     - mood 'aggressive' isn't your 'euphoric' (+0.00)
     - acousticness 0.03, you prefer non-acoustic (+1.94)
     - genre 'metal' isn't your 'edm' (+0.00)
     - positivity 0.30 vs your target 0.85 (+0.45)

4. Storm Runner - Voltline                             5.31 / 10
     - energy 0.91 vs your target 0.95 (+2.88)
     - mood 'intense' isn't your 'euphoric' (+0.00)
     - acousticness 0.10, you prefer non-acoustic (+1.80)
     - genre 'rock' isn't your 'edm' (+0.00)
     - positivity 0.48 vs your target 0.85 (+0.63)

5. Sunrise City - Neon Echo                            5.24 / 10
     - energy 0.82 vs your target 0.95 (+2.61)
     - mood 'happy' isn't your 'euphoric' (+0.00)
     - acousticness 0.18, you prefer non-acoustic (+1.64)
     - genre 'pop' isn't your 'edm' (+0.00)
     - positivity 0.84 vs your target 0.85 (+0.99)


================================================================
  Mellow R&B Romantic
  r&b | romantic | energy 0.50 | non-acoustic | valence 0.60
================================================================

1. Velvet Hours - Amara Soul                           9.12 / 10
     - energy 0.48 vs your target 0.50 (+2.94)
     - matches your mood 'romantic' (+2.50)
     - acousticness 0.40, you prefer non-acoustic (+1.20)
     - matches your favorite genre 'r&b' (+1.50)
     - positivity 0.58 vs your target 0.60 (+0.98)

2. Crown the Block - Verse Kingdom                     4.86 / 10
     - energy 0.78 vs your target 0.50 (+2.16)
     - mood 'confident' isn't your 'romantic' (+0.00)
     - acousticness 0.12, you prefer non-acoustic (+1.76)
     - genre 'hip hop' isn't your 'r&b' (+0.00)
     - positivity 0.66 vs your target 0.60 (+0.94)

3. Night Drive Loop - Neon Echo                        4.70 / 10
     - energy 0.75 vs your target 0.50 (+2.25)
     - mood 'moody' isn't your 'romantic' (+0.00)
     - acousticness 0.22, you prefer non-acoustic (+1.56)
     - genre 'synthwave' isn't your 'r&b' (+0.00)
     - positivity 0.49 vs your target 0.60 (+0.89)

4. Island Time - Sunny Tide                            4.67 / 10
     - energy 0.55 vs your target 0.50 (+2.85)
     - mood 'carefree' isn't your 'romantic' (+0.00)
     - acousticness 0.45, you prefer non-acoustic (+1.10)
     - genre 'reggae' isn't your 'r&b' (+0.00)
     - positivity 0.88 vs your target 0.60 (+0.72)

5. Dusty Porch Swing - Willow Creek Band               4.50 / 10
     - energy 0.50 vs your target 0.50 (+3.00)
     - mood 'nostalgic' isn't your 'romantic' (+0.00)
     - acousticness 0.74, you prefer non-acoustic (+0.52)
     - genre 'country' isn't your 'r&b' (+0.00)
     - positivity 0.62 vs your target 0.60 (+0.98)


================================================================
  Conflicted Listener
  metal | sad | energy 0.30 | acoustic | valence 0.90
================================================================

1. Paper Boats - Hollow Pines                          7.65 / 10
     - energy 0.30 vs your target 0.30 (+3.00)
     - matches your mood 'sad' (+2.50)
     - acousticness 0.90, you like acoustic (+1.80)
     - genre 'folk' isn't your 'metal' (+0.00)
     - positivity 0.25 vs your target 0.90 (+0.35)

2. Spacewalk Thoughts - Orbit Bloom                    5.53 / 10
     - energy 0.28 vs your target 0.30 (+2.94)
     - mood 'chill' isn't your 'sad' (+0.00)
     - acousticness 0.92, you like acoustic (+1.84)
     - genre 'ambient' isn't your 'metal' (+0.00)
     - positivity 0.65 vs your target 0.90 (+0.75)

3. Coffee Shop Stories - Slow Stereo                   5.38 / 10
     - energy 0.37 vs your target 0.30 (+2.79)
     - mood 'relaxed' isn't your 'sad' (+0.00)
     - acousticness 0.89, you like acoustic (+1.78)
     - genre 'jazz' isn't your 'metal' (+0.00)
     - positivity 0.71 vs your target 0.90 (+0.81)

4. Library Rain - Paper Lanterns                       5.27 / 10
     - energy 0.35 vs your target 0.30 (+2.85)
     - mood 'chill' isn't your 'sad' (+0.00)
     - acousticness 0.86, you like acoustic (+1.72)
     - genre 'lofi' isn't your 'metal' (+0.00)
     - positivity 0.60 vs your target 0.90 (+0.70)

5. Autumn Requiem - Elena Marlowe                      5.01 / 10
     - energy 0.22 vs your target 0.30 (+2.76)
     - mood 'melancholic' isn't your 'sad' (+0.00)
     - acousticness 0.97, you like acoustic (+1.94)
     - genre 'classical' isn't your 'metal' (+0.00)
     - positivity 0.21 vs your target 0.90 (+0.31)


================================================================
  Unknown Taste
  k-pop | dreamy | energy 0.60 | non-acoustic | valence 0.70
================================================================

1. Crown the Block - Verse Kingdom                     5.18 / 10
     - energy 0.78 vs your target 0.60 (+2.46)
     - mood 'confident' isn't your 'dreamy' (+0.00)
     - acousticness 0.12, you prefer non-acoustic (+1.76)
     - genre 'hip hop' isn't your 'k-pop' (+0.00)
     - positivity 0.66 vs your target 0.70 (+0.96)

2. Night Drive Loop - Neon Echo                        4.90 / 10
     - energy 0.75 vs your target 0.60 (+2.55)
     - mood 'moody' isn't your 'dreamy' (+0.00)
     - acousticness 0.22, you prefer non-acoustic (+1.56)
     - genre 'synthwave' isn't your 'k-pop' (+0.00)
     - positivity 0.49 vs your target 0.70 (+0.79)

3. Sunrise City - Neon Echo                            4.84 / 10
     - energy 0.82 vs your target 0.60 (+2.34)
     - mood 'happy' isn't your 'dreamy' (+0.00)
     - acousticness 0.18, you prefer non-acoustic (+1.64)
     - genre 'pop' isn't your 'k-pop' (+0.00)
     - positivity 0.84 vs your target 0.70 (+0.86)

4. Gym Hero - Max Pulse                                4.84 / 10
     - energy 0.93 vs your target 0.60 (+2.01)
     - mood 'intense' isn't your 'dreamy' (+0.00)
     - acousticness 0.05, you prefer non-acoustic (+1.90)
     - genre 'pop' isn't your 'k-pop' (+0.00)
     - positivity 0.77 vs your target 0.70 (+0.93)

5. Island Time - Sunny Tide                            4.77 / 10
     - energy 0.55 vs your target 0.60 (+2.85)
     - mood 'carefree' isn't your 'dreamy' (+0.00)
     - acousticness 0.45, you prefer non-acoustic (+1.10)
     - genre 'reggae' isn't your 'k-pop' (+0.00)
     - positivity 0.88 vs your target 0.70 (+0.82)
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



