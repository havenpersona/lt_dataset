from tqdm import tqdm
import lyricsgenius
from youtubesearchpython import *
import csv
import os
from utils import crawl_blog
token = YOUR_GENIUS_TOKEN
genius = lyricsgenius.Genius(token)

lyrics_path = './unprocessed_lyrics/'

with open('meta.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    meta = []
    for row in csv_reader:
        meta.append(row)
meta = meta[1:]

for item in tqdm(meta):
    lid = item[0]
    artist = item[1]
    en_title = item[2]
    kr_title = item[3]
    genre = item[4]
    is_official = item[-2]
    
    if genre == 'k-pop':
        ####################
        #Get English lyrics#
        ####################
        if int(is_official[0]):
            try:
                en_song_api = genius.search_song(en_title + " english version", artist) 
                en_lyrics = en_song_api.lyrics
            except:
                try:
                    en_song_api = genius.search_song(en_title + " english ver", artist) 
                    en_lyrics = en_song_api.lyrics
                except:
                    try:
                        en_song_api = genius.search_song(en_title + " international ver", artist) 
                        en_lyrics = en_song_api.lyrics
                    except:
                        en_song_api = genius.search_song(en_title, artist) 
                        en_lyrics = en_song_api.lyrics

        else:
            if os.path.exists('./processed_lyrics/' + lid + 'en.txt'):
                pass
            else:
                url = item[-1]
                if 'youtu.be' in url:
                    videoInfo = Video.getInfo(url, mode = ResultMode.json)
                    en_lyrics = videoInfo['description']
                elif 'youtube.com' in url:
                    videoInfo = Video.get(url, mode = ResultMode.json, get_upload_date=True)
                    en_lyrics = videoInfo['description']
                elif 'https://malloriemusic.blogspot.com' in url:
                    en_lyrics = crawl_blog(url)
                else:
                    print("error", lid)
                    exit()
        with open(lyrics_path + lid + 'en.txt', 'w') as file:
            file.write(en_lyrics)
        ####################
        #Get Korean lyrics#
        ####################
        if len(kr_title):
            title = kr_title
        else:
            title = en_title
        try:
            try:
                kr_song_api = genius.search_song(title, artist) 
                kr_lyrics = kr_song_api.lyrics
            except:
                kr_song_api = genius.search_song(title + " korean ver", artist) 
                kr_lyrics = kr_song_api.lyrics
            with open(lyrics_path + lid + 'kr.txt', 'w') as file:
                file.write(kr_lyrics)
        except:
            print("Unable to automatically crawl from genius API. Please consider manually obtaining this item.")
            print("Artist : ", artist, "Track Title : ", title, "filepath : ", lyrics_path + lid + 'kr.txt')
    else:
        try:
            en_song_api = genius.search_song(en_title + " english", artist) 
            en_lyrics = en_song_api.lyrics
        except:
            en_song_api = genius.search_song(en_title, artist) 
            en_lyrics = en_song_api.lyrics               
        with open(lyrics_path + lid + 'en.txt', 'w') as file:
            file.write(en_lyrics)
   
        ####################
        #Get Korean lyrics#
        ####################
        if len(kr_title):
            kr_song_api = genius.search_song(kr_title, artist) 
            kr_lyrics = kr_song_api.lyrics
        else:
            kr_song_api = genius.search_song(en_title + " korean", artist) 
            kr_lyrics = kr_song_api.lyrics
        with open(lyrics_path + lid + 'kr.txt', 'w') as file:
            file.write(kr_lyrics)