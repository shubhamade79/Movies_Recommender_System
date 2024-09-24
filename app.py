import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=318950068d02c0404f88480caefd6ac7&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
        return "Photo.jpg" 




def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similary[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_name=[]
    recommended_movies_poster=[]

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)


    return recommended_movies_name,recommended_movies_poster



st.header("Movie Recommendation System Using Machine Learning")
movies=pickle.load(open('movie_list.pkl','rb'))
similary=pickle.load(open('similary.pkl','rb'))


movie_list = movies['title'].values
selected_movies=st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)
if st.button('Show recommendation'):
    recommended_movies_name,recommended_movies_poster=recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
    st.sidebar.markdown("--------")
    st.sidebar.markdown("Developed By  [Shubham Ade](https://github.com/)")
