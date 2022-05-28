import streamlit as st
import pickle as pk
import pandas as pd
import requests as rq
def fetc(movie_id):
    resp=rq.get('https://api.themoviedb.org/3/movie/{}?api_key=f98d54a36dc8a7ebf909d7c9e937e0ae&language=en-US'.format(movie_id))
    data=resp.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']
def recommend(movie):
    movie_index = mv_[mv_['title'] == movie].index[0]
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True, key = lambda k:k[1])[0:20]
    recommended=[]
    recomended_poster=[]
    for v in movie_list:
        movie_id=mv_.iloc[v[0]].movie_id
        # fetch poster from id of the movie
        recommended.append(mv_.iloc[v[0]].title)
        recomended_poster.append(fetc(movie_id))
    return recommended,recomended_poster

movies_dict=pk.load(open('movies_dict.pkl','rb'))
mv_=pd.DataFrame(movies_dict)

similarity=pk.load(open('similarity.pkl','rb'))



st.title('Movie Recommender System')
selected_movie_name =st.selectbox(
    'Which type of movies do you love to see?',
    mv_['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    col6,col7,col8,col9,col10=st.columns(5)
    col11,col12,col13,col14,col15=st.columns(5)
    col16,col17,col18,col19,col20=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    with col11:
        st.text(names[10])
        st.image(posters[10])
    with col12:
        st.text(names[11])
        st.image(posters[11])
    with col13:
        st.text(names[12])
        st.image(posters[12])
    with col14:
        st.text(names[13])
        st.image(posters[13])
    with col15:
        st.text(names[14])
        st.image(posters[14])
    with col16:
        st.text(names[15])
        st.image(posters[15])
    with col17:
        st.text(names[16])
        st.image(posters[16])
    with col18:
        st.text(names[17])
        st.image(posters[17])
    with col19:
        st.text(names[18])
        st.image(posters[18])
    with col20:
        st.text(names[19])
        st.image(posters[19])