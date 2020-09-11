import csv
import sys
import spotipy
import spotipy.util as util
from datetime import date



# GOAL 1 (COMPLETED: 9/10/20): PUT DAILY SHORT TERM TRACK AND ARTIST DATA INTO CSV FILES ON SINGLE LINE
# GOAL 2 (UPDATED: 9/10/20): AUTOMATE RUNNING OF SCRIPT


# append row of data
def append_row(filename, row):
    with open(filename, 'a+', newline='') as track_append:
        csv_writer = csv.writer(track_append)
        csv_writer.writerow(row)


# Info used to get token
username = input('USERNAME: ')
scope = 'user-top-read'
CLIENT_ID = input('CLIENT ID: ')
CLIENT_SECRET = input('CLIENT SECRET: ')
REDIRECT_URI = 'http://localhost:8080'

# get and validate token
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
    sys.exit(0)

# get today's date
today = date.today()

# create list of today's date followed by the id's of my top 50 songs
track_results = sp.current_user_top_tracks(time_range='short_term', limit=50)
track_ids = [today.strftime("%B %d, %Y")]
for item in track_results['items']:
    track_ids.append(item['id'])

# create list of today's date followed by the id's of my top 50 artists
artist_results = sp.current_user_top_artists(time_range='short_term', limit=50)
artist_ids = [today.strftime("%B %d, %Y")]
for item in artist_results['items']:
    artist_ids.append(item['id'])

# appends lists to files
append_row('tastetracker_tracks.csv', track_ids)
append_row('tastetracker_artists.csv', artist_ids)