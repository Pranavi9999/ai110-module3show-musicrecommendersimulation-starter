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

---

Real-world recommenders like Spotify don't rely on a single signal. They blend behavioral data with audio analysis (tempo, energy, acousticness) and contextual signals (time of day, device, activity) to build a continuous picture of taste. The system never asks you directly what you like. It infers it from patterns. This simulation takes a simpler, more transparent approach. Instead of learning from behavior, it uses an explicit user taste profile and scores every song by how closely its audio features match that profile. Rather than optimizing for engagement or retention, it prioritizes interpretability, every recommendation can be directly traced back to a specific feature match, making it easy to understand why a song was or wasn't recommended.

Song features:

- genre
- mood 
- energy 
- tempo_bpm 
- valence 
- danceability 
- acousticness

UserProfile features:

- favorite_genre 
- favorite_mood 
- target_energy 
- likes_acoustic 

## Algorithm Recipe

SCORE(song, user) = genre_score + mood_score + energy_score + acoustic_score

- Genre match  -> +1.5 if song.genre == user.favorite_genre
- Mood match   -> +2.0 if song.mood == user.favorite_mood
- Energy       -> 1.5 × gaussian(user.target_energy, song.energy, σ=0.2)
- Acousticness -> 1.0 × gaussian(0.8 or 0.2, song.acousticness, σ=0.2)

Maximum score: 6.0
Ranking: sort descending, return top 3

---

## Expected Biases

- Mood + genre together control 3.5 of 6.0 points, so a song that sounds
  exactly right but misses both categories will rarely surface.

- likes_acoustic is binary - users who prefer moderate acousticness
  (around 0.5) have no way to express that nuance.

- No diversity mechanism - the same 3 songs appear every time for the
  same user profile, with no variation.

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


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

<<<<<<< HEAD
<a href="C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image.png" target="_blank"><img src='C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image.png' title='Initial Recommendations' width='' alt='Initial Recommendations' class='center-block' /></a>

## Edge case profiles:

Edge case 1:
<a href="C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-1.png" target="_blank"><img src='C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-1.png' title='Edge Case 1' width='' alt='Edge Case 1' class='center-block' /></a>

Edge case 2:
<a href="C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-2.png" target="_blank"><img src='C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-2.png' title='Edge Case 2' width='' alt='Edge Case 2' class='center-block' /></a>

Edge case 3:
<a href="C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-3.png" target="_blank"><img src='C:\Users\prana\Codepath\AI class\ai110-module3show-musicrecommendersimulation-starter\image-3.png' title='Edge Case 3' width='' alt='Edge Case 3' class='center-block' /></a>

=======
![Terminal output showing the recommendations]([image.png](https://github.com/Pranavi9999/ai110-module3show-musicrecommendersimulation-starter/blob/main/image.png))
>>>>>>> fcd0bea072b040a76dcf026bd26bfa58049f0f88
