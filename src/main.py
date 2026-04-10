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

    user_prefs = {
        "genre":        "pop",
        "mood":         "happy",
        "energy":       0.8,
        "likes_acoustic": False,
    }



    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("=" * 50)
    print("  Music Recommender Simulation")
    print("=" * 50)
    print(f"  Genre:    {user_prefs['genre']}")
    print(f"  Mood:     {user_prefs['mood']}")
    print(f"  Energy:   {user_prefs['energy']}")
    print(f"  Acoustic: {user_prefs['likes_acoustic']}")
    print(f"  Catalog:  {len(songs)} songs")
    print("=" * 50)
    print(f"\nTop {len(recommendations)} Recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"       Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"       Score: {score:.2f} / 6.00")
        for reason in explanation.split(" | "):
            print(f"         • {reason}")
        print()


if __name__ == "__main__":
    main()
