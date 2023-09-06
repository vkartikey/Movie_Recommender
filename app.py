import streamlit as st
import pickle
import pandas as pd
import requests

def get_posters(ids):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b654701a6d5a7f1a9bc1fc3a5f74edc4".format(ids)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def get_rating(ids):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b654701a6d5a7f1a9bc1fc3a5f74edc4".format(ids)
    data = requests.get(url)
    data = data.json()
    rating_path = data['vote_average']
    return rating_path

def recommendation_15(title):
    movie_index = movies[movies['title2'] == title].index[0]
    dist = similarity[movie_index]
    recommended = sorted(list(enumerate(dist)), reverse = True, key = lambda x: x[1])[1:16]
    
    rmn = []
    rmp = [] #posters list
    rlst = []
    
    for i in recommended:
        m_id = movies.iloc[i[0]].id
        
        rmn.append(movies.iloc[i[0]].title)
        rmp.append(get_posters(m_id))
        rlst.append(get_rating(m_id))
        
    return rmn, rmp, rlst
        
        
similarity = pickle.load(open('sim_score.pkl', 'rb'))
movies_dictionary = pickle.load(open('movies_raw.pkl', 'rb'))
movies = pd.DataFrame(movies_dictionary)

movies_list = movies['title2'].values


st.title(':popcorn: :orange[Popcorn] & :blue[Chill] :ice_cube:')
st.subheader("Movie Recommendation System", divider= "rainbow")
selected_movie = st.selectbox(
    'You want to watch movies like:',
    (movies_list))

if st.button("Suggest Me Some Movies!", type="primary"):
    
    st.write(":sunglasses: Here are my suggestions for :fire:", selected_movie, ":fire:")
    rmn, rmp, rlst = recommendation_15(selected_movie)
  
        
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.write(rmn[0])
            st.image(rmp[0])
            st.write("Rating:", rlst[0])
        
        with col2:
            st.write(rmn[1])
            st.image(rmp[1])
            st.write("Rating:", rlst[1])
        
        with col3:
            st.write(rmn[2])
            st.image(rmp[2])
            st.write("Rating:", rlst[2])
        
        with col4:
            st.write(rmn[3])
            st.image(rmp[3])
            st.write("Rating:", rlst[3])
        
        with col5:
            st.write(rmn[4])
            st.image(rmp[4])
            st.write("Rating:", rlst[4])
    
    st.divider()
    
    with st.container():
        col6, col7, col8, col9, col10 = st.columns(5)
        with col6:
            st.write(rmn[5])
            st.image(rmp[5])
            st.write("Rating:", rlst[5])
            
        with col7:
            st.write(rmn[6])
            st.image(rmp[6])
            st.write("Rating:", rlst[6])
            
        with col8:
            st.write(rmn[7])
            st.image(rmp[7])
            st.write("Rating:", rlst[7])
            
        with col9:
            st.write(rmn[8])
            st.image(rmp[8])
            st.write("Rating:", rlst[8])
            
        with col10:
            st.write(rmn[9])
            st.image(rmp[9])
            st.write("Rating:", rlst[9])
            
    
    st.divider()
    
    with st.container():
        col11, col12, col13, col14, col15 = st.columns(5)  
    
        with col11:
            st.write(rmn[10])
            st.image(rmp[10])
            st.write("Rating:", rlst[10])
            
        with col12:
            st.write(rmn[11])
            st.image(rmp[11])
            st.write("Rating:", rlst[11])
            
        with col13:
            st.write(rmn[12])
            st.image(rmp[12])
            st.write("Rating:", rlst[12])
            
        with col14:
            st.write(rmn[13])
            st.image(rmp[13])
            st.write("Rating:", rlst[13])
            
        with col15:
            st.write(rmn[14])
            st.image(rmp[14])
            st.write("Rating:", rlst[14])