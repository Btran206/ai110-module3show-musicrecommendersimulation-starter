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

    #Starter example profile
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


    # Edge Case 1: Single categorical field, all others absent
    # Only "genre" is provided, so mood/energy/acoustic are all skipped.
    # Every lofi song scores exactly 0.35; every other song scores 0.00.
    # There are 3 lofi songs in the catalog requesting top 3 fills the list entirely
    # with ties.
    # user_prefs = {"genre": "lofi"}

    # print(f"\nUser preferences: {user_prefs}")
    # recommendations = recommend_songs(user_prefs, songs, 5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()

    # # Edge Case 2: Genre and mood that do not exist in the catalog
    # # bossa nova and zen match zero songs, so both categorical weights (0.35 + 0.25 = 0.60)
    # # contribute nothing. Only energy proximity (0.25) and acoustic preference (0.15) drive
    # # the ranking. Tests if the system still differentiate on partial signals
    # user_prefs = {
    #     "genre": "bossa nova",
    #     "mood": "zen",
    #     "energy": 0.5,
    #     "acoustic": True,
    # }

    # print(f"\nUser preferences: {user_prefs}")
    # recommendations = recommend_songs(user_prefs, songs, 5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()

    # # Edge Case 3: Contradictory / self-fighting profile
    # # Genre + mood point squarely at Iron Collapse (metal, aggressive, energy=0.97, acousticness=0.03),
    # # but energy=0.0 and acoustic=True pull toward the opposite side.
    # user_prefs = {
    #     "genre": "metal",
    #     "mood": "aggressive",
    #     "energy": 0.0,
    #     "acoustic": True,
    # }
    
    # print(f"\nUser preferences: {user_prefs}")
    # recommendations = recommend_songs(user_prefs, songs, 5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()


if __name__ == "__main__":
    main()
