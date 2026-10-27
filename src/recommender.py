import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# Feature weights, in priority order. The maximum possible score is their sum (10.0).
ENERGY_WEIGHT = 3.0
MOOD_WEIGHT = 2.5
ACOUSTIC_WEIGHT = 2.0
GENRE_WEIGHT = 1.5
VALENCE_WEIGHT = 1.0
MAX_SCORE = ENERGY_WEIGHT + MOOD_WEIGHT + ACOUSTIC_WEIGHT + GENRE_WEIGHT + VALENCE_WEIGHT

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: Optional[float] = None  # 0-1 positivity target; None means no preference

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    float_fields = ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def closeness(value: float, target: float) -> float:
    """Returns 1.0 for an exact match, falling linearly toward 0.0 as the gap grows (0-1 features)."""
    return max(0.0, 1.0 - abs(value - target))

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py

    score = 3.0 * energy closeness
          + 2.5 * mood match
          + 2.0 * acoustic fit
          + 1.5 * genre match
          + 1.0 * valence closeness

    Returns the total score and one reason per feature showing the points it contributed.
    Features missing from user_prefs are skipped.
    """
    score = 0.0
    reasons = []

    if "energy" in user_prefs:
        points = ENERGY_WEIGHT * closeness(song["energy"], user_prefs["energy"])
        score += points
        reasons.append(
            f"energy {song['energy']:.2f} vs your target {user_prefs['energy']:.2f} (+{points:.2f})"
        )

    if "mood" in user_prefs:
        if song["mood"].lower() == user_prefs["mood"].lower():
            points = MOOD_WEIGHT
            reasons.append(f"matches your mood '{song['mood']}' (+{points:.2f})")
        else:
            points = 0.0
            reasons.append(f"mood '{song['mood']}' isn't your '{user_prefs['mood']}' (+0.00)")
        score += points

    if "likes_acoustic" in user_prefs:
        if user_prefs["likes_acoustic"]:
            points = ACOUSTIC_WEIGHT * song["acousticness"]
            label = "you like acoustic"
        else:
            points = ACOUSTIC_WEIGHT * (1.0 - song["acousticness"])
            label = "you prefer non-acoustic"
        score += points
        reasons.append(f"acousticness {song['acousticness']:.2f}, {label} (+{points:.2f})")

    if "genre" in user_prefs:
        if song["genre"].lower() == user_prefs["genre"].lower():
            points = GENRE_WEIGHT
            reasons.append(f"matches your favorite genre '{song['genre']}' (+{points:.2f})")
        else:
            points = 0.0
            reasons.append(f"genre '{song['genre']}' isn't your '{user_prefs['genre']}' (+0.00)")
        score += points

    if "valence" in user_prefs:
        points = VALENCE_WEIGHT * closeness(song["valence"], user_prefs["valence"])
        score += points
        reasons.append(
            f"positivity {song['valence']:.2f} vs your target {user_prefs['valence']:.2f} (+{points:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
