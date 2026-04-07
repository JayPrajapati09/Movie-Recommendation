# Movie-Recommendation

This Project Displaying TF-IDF vectorization with cosine similarity to show similar movies based on their plots.

---

### DataSet
This dataset was scraped from wikipedia containing following columns.

**Release Year**,**Title**,**Origin/Ethnicity**,**Director**,**Cast**,**Genre**,**Wiki Page**,**Plot**.

---

### The Challange 
Sample plot : Movie Name - The Martyred Presidents (1901)
plot : The_Martyred_Presidents,"The film, just over a minute long, is composed of two shots. In the first, a girl sits at the base of an altar or tomb, her face hidden from the camera. At the center of the altar, a viewing portal displays the portraits of three U.S. Presidents—Abraham Lincoln, James A. Garfield, and William McKinley—each victims of assassination.

Seeeing the plot I have applied simple NLP pipeline for making word vectors for calculating TF-IDF Vectorization and Made a cosine similarity Matrix for similar 10 movies based on similarity.

---

### Streamlit 
You can checkout strreamlit demo for this app.
[Ready to Watch](https://ready-to-watch.streamlit.app/) 