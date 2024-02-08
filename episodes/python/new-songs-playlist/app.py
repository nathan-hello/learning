import code
import flask
import spotipy
import spotipy.oauth2   
import os
from secret import spotify_oauth



app = flask.Flask(__name__)
app.secret_key = 'poihbuawfer98h0'
app.config['SESSION_COOKIE_NAME'] = 'cookie'




@app.route('/')
def login():
    auth_url = spotify_oauth().get_authorize_url()
    print(auth_url)
    # user_spot_oauth = spotify_oauth()
    # auth_url = user_spot_oauth.get_authorize_url()
    return flask.redirect(auth_url)

@app.route('/callback')
def callback():
    user_spot_oath = spotify_oauth()
    flask.session.clear()
    web_code = flask.request.args.get('code')
    token_code = user_spot_oath.get_access_token(web_code)
    flask.session[code.TOKEN_INFO] = token_code
    return flask.redirect(flask.url_for('tracks', _external=True))

@app.route('/tracks')
def tracks():
    # string = ''
    # idx = 1
    # for item in code.smaller_dict('liked_songs'):
    #     string += f'{idx} {str(item)}'
    #     string += '<br/>'
    #     idx += 1
    # x = code.big_dict()['num_of_liked_songs']
    # string += str(x)

    # return string
    return code.big_dict()['liked_songs']
    



 


if __name__ == '__main__':
    app.run()