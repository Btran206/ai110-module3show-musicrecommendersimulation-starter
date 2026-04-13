# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Music Wizard**

---

## 2. Intended Use  

Music Wizard generates song recommendations from a fixed catalog based on a user's taste preference. It is designed for classroom exploration not production use. The model assumes the user can accurately describe their own preferences upfront (favorite genre, mood, energy level, and whether they like acoustic music), and that those stated preferences good representation for what they will actually enjoy. It makes no attempt to learn from listening history, skips, or any real behavioral signal.

---

## 3. How the Model Works  

Every song in has a set of descriptive tags like its genre, mood, how energetic it sounds, and how acoustic it is. The user provides a taste profile or their favorite genre and mood, a target energy level on a scale from 0 to 1, and whether they lean toward acoustic music. The system then goes through every song and tries to find a song that matches user preferences. For each of those four features a match will assign credit based on how close the match is, and adds it all up into a single score between 0 and 1. Genre and mood will be scored by either a match or not. Energy and acousticness are scored on a scale based on how far the song is from what the user wants. The songs are then sorted by the resulting score and the top results are returned.

I later refined the starter logic to add proximity bubbles for genre and mood, a soft multiplier for acoustic fit, and a valence tiebreaker. Songs genre and moods shouldn't just be an all or nothing, pop and indie-pop should be considered adjacent which is why the scoring was updated to give partial credit, similar for mood. Adding a soft multiplier for acoustic fit is better here because the penalty was too strict if a user did not want acoustic music. A tiebreaker was added for when songs end up with the same score. Rather than falling back on whichever song happened to appear first in the data file, the tiebreaker looks at the mood context. If you asked for something happy or uplifting, tied songs are then ranked by flavor.

---

## 4. Data  

The dataset contains 20 songs with genres like pop, lofi, rock, jazz, classical, hip-hop, etc. Moods include happy, chill, intense, relaxed, focused, melancholic, and much more. No songs were added or removed from the starter dataset. The dataset is missing a lot of what makes music taste complex. There are no subgenre distinctions and the dataset heavily skews toward Englishl Western genres. Someone who listens to K-pop or classical Indian music would find nothing relevant here.

---

## 5. Strengths  

The system works best for users with well represented preferences. Someone who knows they want chill lofi with low energy and an acoustic feel will get exactly that. The energy and acousticness sliding scale does a decent job of surfacing sonically similar songs even when the genre or mood label doesn't match perfectly. For my example user preference with genre: lofi, mood: chill, energy: .35, and acoustic: true, is an example of a very well represented preference profile, the top recommendations returned a chill lofi song called Library Rain as the top recommendation.

---

## 6. Limitations and Bias 

The system ignores valence, danceability, and tempo. A deeply sad song and a euphoric one will score identically if their other features match. Genre carries 35% of the total score, which means a single categorical match can outweigh a song with a perfect match for energy and acousticness. Binary genre matching means indie pop and pop are treated as completely unrelated, penalizing users with niche or hybrid tastes. Users whose preferences align with the most common genres in the dataset (pop, lofi, rock) are naturally better served because there are more songs for those categories to compete and differentiate on. Anyone with cross genre or non Western preferences gets very little out of this model due to the dataset.

---

## 7. Evaluation  

I tested three edge case profiles: a genre-only lofi input with no other fields, entirely unseen genre and mood, and a contradictory profile requesting metal and aggressive genre/mood alongside energy=0.0 and acoustic=True. For each I looked at whether the top results made intuitive sense and whether the ranking order was stable. I also ran a weight experiment — halving genre from 0.35 to 0.175 and adding that onto energy to bring it to 0.425 to see how sensitive the rankings were to weight choices. The most surprising result was in Test Case 3: under the original weights Iron Collapse (the only metal/aggressive song) ranked #1 despite being a nearly perfect mismatch on energy and acousticness. Under the shifted weights it dropped to #4, which felt more honest given the profile.

---

## 8. Future Work  

The most impactful next step would be adding genre proximity a small lookup that knows jazz is closer to blues than to metal so categorical matching isn't just an all or nothing. Incorporating valence and tempo would let the system distinguish emotionally different songs that currently score identically. A tiebreaker rule would make the results less dependent on CSV order. Things like replacing the hand tuned weights with learned weights from actual user feedback would make the system data driven rather than opinion driven. Adding a diversity constraint to prevent the top 5 from being dominated by a single genre would also make the recommendations feel less repetitive.

---

## 9. Personal Reflection  

Building this made me understand that a recommender system is less about math and more about the assumptions hidden inside the math. Every weight I chose had a very big effect on the outcome. The most interesting thing was how much the weight distribution shapes the personality of the recommender. Shifting genre down and energy up produced noticeably different results on the contradictory profile. It made me look at Spotify and YouTube differently. When a recommendation feels off it's probably not a bug it's the system doing learning what matches your preference and what doesn't.
