import time
from spotifyClass import SpotifyRequests
spotify = SpotifyRequests;
# Example program! 



# response = spotify.classInterface("searchForItemRequest", "Consequences", "track", 0)
# print(response.text)

response = spotify.classInterface("changeVolumeRequest", 100)
spotify.classInterface("stopRequest")
spotify.classInterface("stopRequest")
'''


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


        json_data = response.json()
        for device in json_data["devices"]:
            if device["name"] == "LESZKES-KOMP": # For now it's my comp for testing, not rasp for reasons above, might not want to do it here actually
                data["deviceId"] = device["id"] 

        with open("./data/data.json", 'w') as json_file:
            json.dump(data, json_file, indent=2)

'''
