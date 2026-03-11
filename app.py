import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import gdown

# Download files if not present
if not os.path.exists("df.pkl"):
    gdown.download("https://drive.google.com/file/d/16qpXjCTaMA_IbNJVFqwAAeRVn5VHzucd/view?usp=drive_link", "df.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    gdown.download("https://drive.google.com/file/d/1QAyozB0u5vyid7NcarpLAFqFylNsNTsG/view?usp=drive_link", "similarity.pkl", quiet=False)

CLIENT_ID = "998cfc54bf4b4627a5f1e5dcb3f57a9d"
CLIENT_SECRET = "e42a8c18871f43d0a4c24f24cd1ea8c4"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    try:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(f"Album cover found: {album_cover_url}")
        return album_cover_url
    except (IndexError, KeyError, TypeError):
        print("Album cover not found, using fallback.")
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song_name):
    # Match song ignoring case and leading/trailing spaces
    matched_index = music[music['song'].str.strip().str.lower() == song_name.strip().lower()].index

    if matched_index.empty:
        print("Song not found in dataset.")
        return ["Song not found."], ["https://i.postimg.cc/0QNxYz4V/social.png"]

    index = matched_index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_music_names = []
    recommended_music_posters = []

    for i in distances[1:6]:  # Skip self match
        artist = music.iloc[i[0]].artist
        song_title = music.iloc[i[0]].song

        print(f"Recommending: {song_title} by {artist}")

        recommended_music_names.append(song_title)
        recommended_music_posters.append(get_song_album_cover_url(song_title, artist))

    return recommended_music_names, recommended_music_posters


st.header('Music Recommender System')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names,recommended_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])




