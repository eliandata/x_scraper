### X SCRAPER ###

#importing libraries
import streamlit as st
import tweepy
import pandas as pd
from PIL import Image


### CREATING THE APP ###
#image in the sidebar
image = Image.open('Omdena-San-Salvador-Logo.jpeg')
st.sidebar.image(image, caption='Omdena El Salvador Local Chapter')

#title of the app
st.sidebar.title(':blue[X Scraper App]')


# Setting up Twitter API keys
consumer_key = st.sidebar.text_input('API Key')
consumer_secret = st.sidebar.text_input('API SECRET KEY')
access_token = st.sidebar.text_input('Access Token')
access_token_secret = st.sidebar.text_input('Access Token Secret')

# Authentication with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# function for scraping
def scrape_news_tweets(username, num_tweets, csv_filename):
    tweets = []

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items(num_tweets):
        tweets.append([tweet.created_at, tweet.full_text, tweet.favorite_count, tweet.retweet_count, tweet.in_reply_to_status_id])

    df = pd.DataFrame(tweets, columns=['Fecha', 'Título', 'Likes', 'Retweets', 'Comentarios'])

    df.to_csv(csv_filename, index=False, encoding='utf-8')

    return df

# App interface
st.title('Aplicación de Scraper de Twitter')

username = st.text_input('Introduce el nombre de usuario de Twitter del canal de noticias:')
num_tweets = st.number_input('Número de tweets a extraer:', min_value=1, max_value=100, value=10)
csv_filename = st.text_input('Nombre del archivo CSV de salida:', 'news_tweets.csv')

if st.button('Scrapear y almacenar en CSV'):
    df = scrape_news_tweets(username, num_tweets, csv_filename)
    st.success(f'Se han realizado scraping y almacenado {len(df)} tweets de noticias en {csv_filename}.')


st.sidebar.write('Hecho por Elianneth Cabrera')
