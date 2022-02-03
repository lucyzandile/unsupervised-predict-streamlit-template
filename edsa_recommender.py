"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
from email.policy import default
from os import pipe
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

from PIL import Image
import base64

# Importing data
movies = pd.read_csv('resources/data/movies.csv')
train = pd.read_csv('resources/data/ratings.csv')
df_imdb = pd.read_csv('resources/data/imdb_data.csv')

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["About Filtron","Recommender System","Solution Overview","Exploratory Data Analysis","Meet the Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "About Filtron":
        logo = Image.open("resources/imgs/Filtron_App_Logo.png")
        st.image(logo)
        st.title("About Filtron")
        st.write("Filtron is a new innovative tool that uses content based and collaborative filtering techniques to:")
        st.write("Drive traffic to your website, especially through targeted blasts.")
        st.write("Improved user experience by enable users to locate the desired products through appropriate item suggestions.")
        st.write("Reduced workload by analyzing the online behavior of all customers.")
        st.write("Filtron will increase traffic, customer retention, and personalized experiences and this translates to increased sales revenue.")

    
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.image('resources/imgs/content_colab.png',use_column_width=True)
        
        st.write("")
        st.write("")
        st.subheader("Content Based Filtering")
        st.write("Content based recommender is a recommendation model that returns a list of items based on a specific item. The main idea behind content-based filtering is that if a person buys a product A with characteristics X, Y, Z, he is likely to buy any product B with characteristics X, Y, Z.")

        st.write("")
        st.write("")
        st.subheader("Collaborative Based Filtering")
        st.write("The collaborative filtering recommendation technique depends on finding similar users to a target user to make personalized recommendations. The idea behind collaborative filtering is that if a user X buys products A, B, and C. Then another user Y who buys products A and B is also likely to buy product C.")


    if page_selection == "Exploratory Data Analysis":
        st.title("Exploratory Data Analysis")
        st.image('resources/imgs/EDA.png',use_column_width=True)
        #st.info("Exploratory Data Analysis")
        st.markdown("Exploratory data analysis (EDA) is used to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods.We first need to understand our data better, visualise, summarise and interpret the information in the dataset.")
        st.write("")
        st.write("")

        page_options = ["Top 20 movies","Popular cast","Popular directors","Popular movie genres"]
        page_selection = st.selectbox("Choose Option", page_options)
        
        if page_selection == "Top 20 movies":
            #st.subheader("Top 20 popular movies by ratings from year 2000.")
            top_20_movies_ratings = Image.open("resources/imgs/pop_movies.png")
            st.image(top_20_movies_ratings)
            st.write("From the above plot, we observe that the based on average rating and the total count of ratings, the movie Lord of the Rings: The Fellowship of the Ring (2001) had the most rating counts of over 21 000 when we considered movies from 2000 till date.")       
            

        if page_selection == "Popular cast":
            cast_per_appear = Image.open("resources/imgs/cast.png")
            st.image(cast_per_appear)
            st.write("Samuel L Jackson was the popular cast as he appeared in over 80 movies from our database.")
    
        if page_selection == "Popular directors":
            pop_director = Image.open("resources/imgs/director.png")
            st.image(pop_director)
            st.write("Woody Allen was the popular director as he directed over 25 movies from our database.")
            
    
        if page_selection == "Popular movie genres":
            pop_genre = Image.open("resources/imgs/movie_genres.png")
            st.image(pop_genre)
            st.write("The top 5 genres are, in that respect order: Drama, Comedy, Action, Thriller, and Romance.")
    
    
    if page_selection == "Meet the Team":
        st.title("The incredible Team 15")
        st.write("Lucy Zandile Lushaba")
        st.write("Matome Mabotse Selamolela")
        st.write("Thandazani Gazu")
        st.write("Tladi Thaane Thobejane")
        st.write("Winnie Sebapu")
        logo = Image.open("resources/imgs/EDSA_logo.png")
        st.image(logo)
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
