import json
import pandas

with open('data.json', 'r') as j:
    spotify_json = json.load(j)

print(type(spotify_json))

print(spotify_json['liked_songs'][1])