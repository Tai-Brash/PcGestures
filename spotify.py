
import requests
import spotipy
import secrets
import webbrowser
from dotenv import load_dotenv
import os
 
load_dotenv()
 
id = os.getenv('CLIENT_ID')
secret = os.getenv('CLIENT_SECRET')
uri = os.getenv('REDIRECT_URI')

print(uri)
 
getParams = {
    'client_id': id,
    'response_type': 'code',
    'redirect_uri': uri,
    'state': secrets.token_urlsafe(16),
    'scopes': 'user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-private' 
}    
getAuthObj = requests.get('https://accounts.spotify.com/authorize', params=getParams)
 
if getAuthObj.status_code == 200:
    webbrowser.open(getAuthObj.url, new=2)
else:
    print("Was unable to get authorization url.")
 
# postParams = {
#     'grant_type': 'authorization_code',
#     'redirect_uri': 'pc-gestures-login://callback'
# }
# postAuthObj = requests.post('https://accounts.spotify.com/api/token', params=postParams)
# print(postAuthObj)
 
 
