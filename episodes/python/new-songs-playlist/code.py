import json
import flask
import spotipy
import time
from secret import spotify_oauth


#TRY LOOPING OVER THE APPENDED JSON LIST, THEN DOING EVERYTHING ELSE AGAIN
#THIS MIGHT WORK, IF IT DOES RINSE AND REPEAT FOR EVERYTHING ELSE

TOKEN_INFO = 'token_info'

def big_dict():
    spot_dict = {}
    token_info = token_check()
    spot_obj = spotipy.Spotify(auth=token_info['access_token'])

    def get_all_saved_tracks(spot_obj):
        tracks = []
        for x in range(3):
            response = spot_obj.current_user_saved_tracks(limit=3,offset=x)
            if len(response) == 0:
                break
            tracks.append(response)

        return tracks

    # spot_dict['user'] = spot_obj.current_user()
    spot_dict['liked_songs'] = get_all_saved_tracks(spot_obj)
    # spot_dict['liked_songs'] = spot_obj.current_user_saved_tracks()
    # spot_dict['playlists'] = spot_obj.current_user_playlists()
    # spot_dict['saved_albums'] = spot_obj.current_user_saved_albums()
    # spot_dict['num_of_liked_songs'] = spot_obj.current_user_saved_tracks()['total']
    


            

    

    return spot_dict 

def smaller_dict(choice):
    spot_dict = big_dict()
    if choice == 'liked_songs':
        song_list = []
        for track in spot_dict['liked_songs']['items']:
            song = track['track']['name']
            artist = track['track']['album']['artists'][0]['name']
            album = track['track']['album']['name']
            release = track['track']['album']['release_date']
            song_tup = (song, artist, album, release)
            song_list.append(song_tup)
        return spot_dict
    if choice == 'saved_albums':
        album_list = []
        for album in spot_dict['saved_albums']['items']:
            artist_list = []    
            name = album['album']['name']
            for artist in album['album']['artists']: 
                artist_list.append(artist['name'])
            release = album['album']['release_date']
            album_tup = (name, artist_list, release)
            album_list.append(album_tup)
        return album_list
    
def token_check():
    token_info = flask.session.get(TOKEN_INFO, None)
    if not token_info:
        print('user not logged in')
        return flask.redirect('/')
    now = int(time.time())
    token_exp_one_minute = token_info['expires_at'] - now < 60
    if token_exp_one_minute:
        user_spot_oauth = spotify_oauth()
        token_info = user_spot_oauth.refresh_access_token(token_info['refresh_token'])
        print(f'REFRESHED {time.time()}')
    return token_info





# if __name__ == '__main__':
#     info_dict()