"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, MAX_SCORE

LINE_WIDTH = 64


# User taste profiles covering a range of energy levels, moods, and acoustic preferences.
# Keys: genre, mood, energy (0-1 target), likes_acoustic (bool), valence (0-1 target)
USER_PROFILES = {
    "High-Energy Pop Fan": {
        "genre": "pop", "mood": "happy", "energy": 0.85,
        "likes_acoustic": False, "valence": 0.80,
    },
    "Chill Lofi Studier": {
        "genre": "lofi", "mood": "chill", "energy": 0.38,
        "likes_acoustic": True, "valence": 0.60,
    },
    "Intense Rock Head": {
        "genre": "rock", "mood": "intense", "energy": 0.92,
        "likes_acoustic": False, "valence": 0.45,
    },
    "Melancholic Classical Listener": {
        "genre": "classical", "mood": "melancholic", "energy": 0.22,
        "likes_acoustic": True, "valence": 0.20,
    },
    "EDM Party Goer": {
        "genre": "edm", "mood": "euphoric", "energy": 0.95,
        "likes_acoustic": False, "valence": 0.85,
    },
    "Mellow R&B Romantic": {
        "genre": "r&b", "mood": "romantic", "energy": 0.50,
        "likes_acoustic": False, "valence": 0.60,
    },
    # Edge case: preferences that pull in opposite directions
    # (metal is loud and non-acoustic, but this user wants calm, acoustic, upbeat songs).
    "Conflicted Listener": {
        "genre": "metal", "mood": "sad", "energy": 0.30,
        "likes_acoustic": True, "valence": 0.90,
    },
    # Edge case: genre and mood that don't exist in the dataset,
    # so only the numeric features can differentiate songs.
    "Unknown Taste": {
        "genre": "k-pop", "mood": "dreamy", "energy": 0.60,
        "likes_acoustic": False, "valence": 0.70,
    },
}


def print_profile_header(profile_name: str, user_prefs: dict) -> None:
    """Prints a boxed header with the profile name and a one-line summary of its preferences."""
    acoustic = "acoustic" if user_prefs["likes_acoustic"] else "non-acoustic"
    summary = (
        f"{user_prefs['genre']} | {user_prefs['mood']} | energy {user_prefs['energy']:.2f} | "
        f"{acoustic} | valence {user_prefs['valence']:.2f}"
    )
    print("=" * LINE_WIDTH)
    print(f"  {profile_name}")
    print(f"  {summary}")
    print("=" * LINE_WIDTH)


def print_recommendation(rank: int, song: dict, score: float, explanation: str) -> None:
    """Prints one ranked song with its score and each scoring reason on its own line."""
    title = f"{rank}. {song['title']} - {song['artist']}"
    score_text = f"{score:.2f} / {MAX_SCORE:.0f}"
    print(f"{title:<{LINE_WIDTH - len(score_text)}}{score_text}")
    for reason in explanation.split("; "):
        print(f"     - {reason}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print()
        print_profile_header(profile_name, user_prefs)
        print()
        # Each item is (song, score, explanation)
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print_recommendation(rank, song, score, explanation)


if __name__ == "__main__":
    main()
