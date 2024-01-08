import time
from spotifyClass import SpotifyRequests
spotify = SpotifyRequests;
# Example program! 

spotify.classInterface("playRequest") # Start playing the music
spotify.classInterface("stopRequest") # Stop playing the msuic
response = spotify.classInterface("playlistsRequest")
json_data = response.json()
for playlist in json_data["items"]:
    if playlist["name"] == "JoJo OST":
        playlistId = playlist["id"] 

response = spotify.classInterface("playlistContentRequest", playlistId)

offset = 0
json_data = response.json()
for song in json_data["tracks"]["items"]:
    if song["track"]["name"] == "Killer":
        offset += 1
    else:
        break
response = spotify.classInterface("availableDevicesRequest") # Saves (right now my computer, change to raspberry) id to data.json
print(response.text)
spotify.classInterface("transferPlaybackRequest") # Transfer playing to device that is in data.jsonS
time.sleep(2)
spotify.classInterface("playRequest", playlistId, offset)

