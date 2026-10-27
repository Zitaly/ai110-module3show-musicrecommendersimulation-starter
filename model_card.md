# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

AGSRecommender
(Another Generic Song Recommender)

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for.  

This recommender, intended for classroom exploration, is designed to recommend songs based primarily on energy, mood, and acousticness.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

The program looks at and scores in the order of energy, mood, acousticness, genre, and valence. These scores are multiplied by their weights anda added up to a max of 10. A high score means a good recommendation.
---

## 4. Data  

Describe the dataset the model uses.  
 
The dataset contains 18 songs, and it consists of a broad range of genres. Because of how broad musical genres are, even excluding sub-genres, many tastes aren't represented.
---

## 5. Strengths  

Where does your system seem to work well   

The system does well at broadly recommending music for a specific user. The genres and energy tend to match what someone may want.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The dataset has uneven representation. Some tastes have more represenation that other tastes, and these overrepresented tastes will consistently have higher scores than underrepresented ones. As a result, mainstream music is favored over niche music, and this in turn favors those who like mainstream music.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

High-energy pop fan prefers non-acoustic, happy songs; chill lofi studier prefers low energy, acoustic songs that have some positivity; intense rock head likes extremely high energy with low positivity; and the melancholic classical listener wants low energy and low positivity.

The results didn't really surprise me.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would improve the model by increasing the nuance of how things are judged. This includes addressing sub-genres, like pop vs indie pop, and going for targets instead of simple yes/no decisions. Additionally, I would add more points to the dataset to remove the uneven representation and generate better test data.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment during this project was seeing how quickly AI can work at testing, creating, gathering data, and interpreting data when a plan is properly made and outlined.

Simple algorithms involve a lot of complexity that can still result in them being wrong. I think the training is a constant, complex process that can't ever end without everything falling apart.

I would try fixing the current issues and adding real songs.