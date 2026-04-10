# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**Spotify VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and acousticness preference. It is designed for classroom exploration — not real users — to demonstrate how a content-based scoring system works and where it breaks down.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system scores every song by checking four things: does the genre match, does the mood match, how close is the energy, and how acoustic is the song. Each match earns points. The song with the most points gets recommended.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The catalog has 18 songs. The starter file had 10, 8 more were added to cover genres like metal, country, r&b, blues, hip-hop, classical, funk, and folk. Moods represented include happy, chill, intense, relaxed, focused, moody, angry, nostalgic, romantic, melancholic, energetic, sad, euphoric, and dreamy. The dataset skews toward chill and low-energy music, and has no representation of electronic subgenres like EDM or house. It also reflects a narrow cultural range, mostly Western genres, so users outside that taste space will get poor results.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It works best when the user's genre and mood exist in the catalog and their energy preference is close to at least a few songs. Alex's profile (lofi, chill, low energy) produced an immediately obvious top 2, the right songs rose to the top with a clear score gap between them and the rest of the list.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system over-prioritizes categorical matches — mood and genre together control 2.75 of 6.75 points before any audio feature is considered. This means users whose preferred genre or mood doesn't exist in the catalog (like "reggae" or "grateful") silently lose nearly half their possible score, making the top results nearly indistinguishable from each other. This was confirmed by running The Ghost profile, where all five recommended songs clustered within 0.3 points of each other, giving the false impression of a meaningful ranking. A real system would detect when no categorical matches are found and warn the user that results are low-confidence.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Three profiles were tested across different scenarios. Alex (lofi, chill, energy 0.38, likes_acoustic True) worked as expected — Library Rain and Midnight Coding dominated the top results, which confirmed the scoring logic was correct for a clean, consistent profile. The Ghost (reggae, grateful, energy 0.5, likes_acoustic False) was the most surprising — with no genre or mood matches in the catalog, all five recommended songs scored within 0.3 points of each other, making the ranking feel meaningless even though the system returned results confidently. The Acoustic Trap (metal, angry, energy 0.97, likes_acoustic True) revealed that genre and mood bonuses are strong enough to overcome a heavy acousticness penalty — Hollow Bones ranked #1 despite having acousticness of 0.04 against a target of 0.8, which showed that the likes_acoustic field has less real influence than expected.

Alex vs. The Ghost — Alex matched genre and mood immediately, so top results were obvious. The Ghost matched nothing, so all five results scored within 0.3 points of each other — the ranking looked confident but was nearly random.

Alex vs. The Acoustic Trap — opposite ends of the catalog. Even though the Acoustic Trap user said they liked acoustic music, Hollow Bones (acousticness 0.04) still ranked #1 because genre and mood bonuses outweighed the acousticness penalty.

Why Gym Hero keeps appearing for Happy Pop users — it's a pop song with high energy, so it collects the genre bonus and scores close enough on energy to rank high. The system can't tell the difference between "fun pop" and "workout pop" — that distinction lives in meaning, not numbers.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
- Add target_valence to the user profile so users can express "chill but uplifting" vs "chill but melancholic"
- Replace likes_acoustic: bool with a float so users can prefer moderate acousticness instead of just yes or no
- Add a diversity rule that blocks the same artist from appearing twice in the top results
- Show a confidence warning when no genre or mood matches are found, so the user knows the results are low-quality
- Add more songs to reduce catalog skew toward chill and low-energy genres

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this showed how much small weight decisions matter — changing genre from 1.5 to 0.75 visibly shifted which songs surfaced. The most surprising thing was that the system returned confident-looking results even when it had no real signal, like with The Ghost profile. That made me realize real apps must have fallback logic for low-confidence situations, because a ranked list always looks authoritative even when it isn't.

The biggest learning moment was realizing the scoring rule is just opinions disguised as math, choosing mood over genre isn't neutral, it's an assumption that shapes every result.
AI tools helped with the logic and coding but I still had to double-check the code myself. A lot of the times AI would just ask if it could make the changes without showing me what the changes were.

What surprised me was how much a simple point system feels like a real recommendation. When the right songs rose to the top for Alex, it felt intelligent, even though it was just arithmetic on a CSV.

Next I would make the profile update based on skips and replays, so the system learns instead of just matching what the user declared upfront.