"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


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


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {profile_name} ===")
        print(f"Preferences: {user_prefs}\n")
        for rec in recommendations:
            # Each item is (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
