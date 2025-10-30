import pandas as pd
import streamlit as st
import pickle

st.title("Movie Recommendation App")
st.write("Get movie recommendations based on your favorite movie.")

df = pd.read_csv("wiki_movie_plots_deduped.csv")

with open("movie_top_k.pickle", "rb") as file:
    model = pickle.load(file)

## 1. Movie Selection
movie_list = df['Title'].values
selected_movie = st.selectbox("Select a movie you like:", movie_list)

## if movie is not found tell user to select a valid movie
if selected_movie not in movie_list:
    st.error("Movie not found. Please select a valid movie from the list.")
    st.stop()

## 2. Show Selected Movie Info (Collapsible)
with st.expander("Show Selected Movie Info"):
    # Find the movie info
    movie_info = df[df['Title'] == selected_movie].iloc[0]
    
    st.write(f"**Title:** {movie_info['Title']}")
    st.write(f"**Release Year:** {movie_info['Release Year']}")
    st.write(f"**Origin/Ethnicity:** {movie_info['Origin/Ethnicity']}")
    st.write(f"**Director:** {movie_info['Director']}")
    st.write(f"**Cast:** {movie_info.get('Cast', 'N/A')}") # Use .get for safety
    st.write(f"**Genre:** {movie_info['Genre']}")
    st.write(f"**Wiki Page:** {movie_info['Wiki Page']}")
    st.write(f"**Plot:** {movie_info['Plot']}")


## 3. Recommendation Function 
def get_recommendations(movie_title, model_df, df, top_k=10):
    
    movie_idx = df.index[df['Title'] == movie_title][0]
    
    recommendation_row = model_df.iloc[movie_idx]

    recommended_movies = []
    for rec_list in recommendation_row:
        rec_index = rec_list[0]  
        rec_score = rec_list[1] 
        
        rec_title = df.iloc[rec_index]['Title'] 
            
        recommended_movies.append({
            'Title': rec_title, 
            'Similarity Score': rec_score
        })
        
    rec_df = pd.DataFrame(recommended_movies)
    
    rec_df = rec_df.sort_values(by='Similarity Score', ascending=False)
    
    return rec_df.head(top_k)


## 4. Get and Display Recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movie, model, df, top_k=10)
    
    st.write("### Recommended Movies:")
    
    
    rec_display = recommendations.copy()
    
    rec_display['Similarity Score'] = rec_display['Similarity Score'] * 100
    
    min_val = 0.0
    max_val = 100.0 

    st.dataframe(
        rec_display,
        column_config={
            "Title": "Movie Title",
            "Similarity Score": st.column_config.ProgressColumn(
                label=f"Similarity to {selected_movie}",
                
                help="How similar this movie is to your selection.",
                
                format="%d%%", 
                
                min_value=min_val,
                max_value=max_val,
            )
        },
        hide_index=True,
        use_container_width=True
    )
