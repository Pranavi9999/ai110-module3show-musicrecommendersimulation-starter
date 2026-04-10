from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import math


def gaussian(preference: float, value: float, sigma: float = 0.2) -> float:
    """Returns a 0–1 similarity score that peaks at 1.0 when value equals preference."""
    return math.exp(-((preference - value) ** 2) / (2 * sigma ** 2))


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences and returns (total_score, reasons)."""
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs.get("genre"):
        score += 0.75
        reasons.append("genre match (+1.5)")

    # Mood match
    if song["mood"] == user_prefs.get("mood"):
        score += 2.0
        reasons.append("mood match (+2.0)")

    # Energy similarity
    energy_sim = gaussian(user_prefs.get("energy", 0.5), song["energy"], sigma=0.2)
    energy_points = round(3.0 * energy_sim, 2)
    score += energy_points
    reasons.append(f"energy similarity ({song['energy']} vs {user_prefs.get('energy', 0.5)}) (+{energy_points})")

    # Acousticness similarity
    acoustic_target = 0.8 if user_prefs.get("likes_acoustic", False) else 0.2
    acoustic_sim = gaussian(acoustic_target, song["acousticness"], sigma=0.2)
    acoustic_points = round(1.0 * acoustic_sim, 2)
    score += acoustic_points
    reasons.append(f"acousticness similarity ({song['acousticness']} vs target {acoustic_target}) (+{acoustic_points})")

    return round(score, 2), reasons

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
    """Reads songs.csv and returns a list of dicts with numeric fields cast to float/int."""
    import csv

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song, sorts by score descending, and returns the top k results."""
    scored = []
    for song in songs:
        total, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        scored.append((song, total, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
