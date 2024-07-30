import requests
from bs4 import BeautifulSoup
URL="https://www.billboard.com/charts/hot-100/"
date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response=requests.get(URL+date)  
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")

all_songs=soup.select("li ul li h3")
song_titles=[song.getText().strip() for song in all_songs]
print(song_titles)
