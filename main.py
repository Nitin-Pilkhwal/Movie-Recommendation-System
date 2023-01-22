#importing some libraries
import pickle
import streamlit as st
import requests
import pandas as pd

#function to fetch poster from TMBD database

def fetch_poster(movie_id):
    API_key= '9b933ef7d90adbfb974c67f14710e36c'
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id,API_key))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    movie_link=[]
    recommended_movies=[]
    recommended_movies_posters = []
    for i in movies_list1:
        movie_id=movies.iloc[i[0]].id
        movie_link.append(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters,movie_link

st.header('Movie Recommendation System')
movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


#Here is the main Streamlit code which design the front of our webapp.

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters,links = recommend(selected_movie)
    # col1, col2, col3, col4, col5 = st.columns(5,gap="medium")
    col1, col2 ,col3= st.columns(3,gap="medium")

    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[0]))
    with col1:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[2]))

    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[1]))
    with col2:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[3]))

    with col3:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[4]))
    with col3:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movie_names[5])
        st.write("[click here](https://www.themoviedb.org/movie/{}) to know more".format(links[5]))
