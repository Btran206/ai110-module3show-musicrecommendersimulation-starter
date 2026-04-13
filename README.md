# 🎵 Music Recommender Simulation

## Project Summary

I built a simple music recommender that scores songs against a user's taste profile using four features: genre, mood, energy level, and acousticness. Each feature carries a fixed weight, and the system ranks every song by how closely it matches the user's preferences, then returns the top k results.

---

## How The System Works

Unlike Spotify or YouTube, which uses advanced machine learning techniques that score from various features like clicks, skips, likes, and sound profile before running them through a complex ML pipeline, my recommender takes a simpler approach. It doesn't know anything about what other people like. It only knows the current user, and tries to find songs that match their taste directly.

Each song carries a set of descriptive features like genre, mood, energy level, acousticness, tempo, valence, and danceability. The user profile stores the things that matter most for example, their favorite genre and mood, how energetic they like their music, and whether they tend to prefer acoustic sounds.

When scoring a song, the system compares those profile preferences against the song's features using a simple weighted formula. Genre match matters most (35%), followed by mood (25%), energy (25%), and acousticness (15%). Valence, danceability, and tempo are will be used for future experimentation.

Once every song has a score, the system sorts them highest to lowest and returns the top 5. The final score sits between 0.0 and 1.0, which represents the predicted percentage match for the user preference and the song.

![Recommender Flowchart](images/recommender_flowchart_starter.png)

## Known Biases

- Genre has a 35% weighting, so a genre match alone can outscore a song that nails mood, energy, and acousticness but has the wrong genre.
- Genre and mood use exact string comparison, so indie pop ≠ pop scores 0 despite being closely related. There is no concept of genre or mood proximity. I can address this with transformations to the song genre before being fed into the recommender.
- Valence, danceability, and tempo aren't being utilized in the recommender. A deeply sad song and an upbeat one score identically if their other features match, which can produce recommendations that feel tonally wrong. I will experiment with these features if I have the time.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

  ```bash
  python -m venv .venv
  source .venv/bin/activate      # Mac or Linux
  .venv\Scripts\activate         # Windows
  ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```
python src/main.py
```

Example Output:

![Terminal Output](images/terminal_output.png)

### Running Tests

Run the starter tests with:

```bash
pytest
```

---

## Experiments

I will be testing edge cases and model sensitivity within this section. The first image will be the default model while the second image will be the model with a weight shift from genre dominant to energy dominant.

### Edge Case 1 — Single categorical field

Because Python's sort is stable, tied songs are returned in their original CSV insertion order. The system produces a ranked list with zero real differentiation among the top results. There is no tiebreaker logic, so the winner among equally scored songs is an determined soley by data order, not preference alignment.

![Test 1](images/test1.png)

After running a weight shift from genre's .35 to .175 and energy from .25 to .425, the single genre bias remains the same.

![Test 1](images/test1V2.png)

---

### Edge Case 2 — Genre and mood that don't exist

The system returns results, but the compressed score means all songs cluster closely together. Small differences in energy proximity become the primary differentiator, which can surface non-obvious winners (a mid energy synthwave track Night Drive beating a folk track Empty Porch because because intuitively, folk should be closer to bossa nova and zen). This shows how heavily the system depends on categorical hits to produce intuitive results.


![Test 2](images/test2.png)

For test case 2, although the outputs are different, the system still relies on categorical features to drive intuitive results. Another issue came up here which exposes tiebreaker logic again because rankings are sorted purely by insertion order. 

![Test 2](images/test2V2.png)

---

### Edge Case 3 — Contradictory / self-fighting profile 

When categorical weights sum to 0.60 the remaining 0.40 of continuous features cannot overcome even at maximum disagreement. A user who genuinely wants quiet acoustic music but states metal/aggressive as their genre/mood will consistently receive recommendations that contradict their continuous preferences. This confirms the over reliance on categorical matching noted in Known Biases.

![Test 3](images/test3.png)

For test case 3, the recommendations look alot more balanced. Iron Collapse was not skewed to the top for having a dominating genre match when presented with low energy and acoustic profile.

![Test 3](images/test3V2.png)


---

## Limitations and Risks

The recommender operates on a dataset of only 20 songs, which is too small to find meaningful diversity or handle niche preferences. It relies entirely on four weighted features (genre, mood, energy, acousticness) with no learning from actual user behavior, so the weights are fixed guesses rather than data driven signals. Categorical features like genre and mood are binary where a song either matches or it doesn't which means the system cannot reason about song proximity (jazz being closer to blues than to metal). The model also has no tiebreaker logic, so songs with identical scores are ranked by their insertion order in the CSV rather than any preference signal.

---

## Reflection

Building this recommender made me realize that for my version at least is really just a formalized opinion. I decided what features matter, assigned them weights, and that choice shapes the result the system produces. Genre being worth 35% is a design decision and users will never see it or know why. This is the part that stuck with me most because the math looks objective on the surface, but the assumptions are the real drivers for these systems.

The bias was harder to see until I ran the edge cases and exposed these glaring issues. The binary categorical matching means the system has no sense of closeness between genres for example jazz and blues score the same as jazz and metal when neither matches. This can be a disadvantage for users with niche or cross genre tastes. Bias also presents itself with feature dominance in this case genre which overshadows other features like energy and acousticness even if they are a perfect fit. I didn't designed this model with these consequences in mind, more so how I important I felt these features were. In a larger system trained on user behavior, that same problem can show up if certain genres or moods are underrepresented in the training data. The model will learn to underserve those users and nobody will notice.


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

