"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile — low energy, chill, acoustic-leaning user.
    # This creates a clear spread: lofi/folk/classical score high,
    # rock/metal/edm score low, making it easy to verify the system works.

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    print(f"\nUser preferences: {user_prefs}")
    recommendations = recommend_songs(user_prefs, songs, 3)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    

    user_prefs = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "acoustic": True,
    }

    print(f"\nUser preferences: {user_prefs}")
    recommendations = recommend_songs(user_prefs, songs, 3)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
