import requests
from bs4 import BeautifulSoup
import spotipy
from dotenv import load_dotenv
load_dotenv()
from spotipy.oauth2 import SpotifyOAuth
import os 
date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response=requests.get(os.getenv("SPOTIPY_REDIRECT_URI")+date)  
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")
all_songs=soup.select("li ul li h3")
song_titles=[song.getText().strip() for song in all_songs]
scope="playlist-modify-private"
2
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_ID"),
        client_secret=os.getenv("SPOTIPY_SECRET_ID"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
result=sp.current_user()["id"]
track_uris=[]
year=date.split("-")[0]
for song in song_titles:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist=sp.user_playlist_create(user=result, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=create_playlist["id"], items=track_uris)