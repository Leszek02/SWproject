import json
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from spotifyClass import SpotifyRequests


app = Flask(__name__, template_folder='WebPage') # WebPage is a folder for all pages
CORS(app)

@app.route('/') # Spotify redirects here, needs this to scrap the auth code
def redirectPath():
    if 'code' in request.args: 

        with open("./data/data.json", 'r') as json_file:
            data = json.load(json_file)

        data["clientCode"] = request.args.get('code') 

        with open("./data/data.json", 'w') as json_file:
            json.dump(data, json_file, indent=2)

        spotify.accessTokenRequest() # use client code to receive access token and refresh token
    return redirect(url_for('mainPage')) # redirect user to mainPage


@app.route('/main') # This is temporary the main page
def mainPage():
    app.logger.info('Rendering page')
    return render_template('index.html');


@app.route('/getAuthorizationRequest') # Execute authorization methods
def receiveAuthUrl():
    url = spotify.authorizationRequest()
    return {"url": url} # return spotify authentication URL (needs to be done once, if we have auth code saved it can be used as long as the user does not delete it)


# Main program here
if __name__ == '__main__':
    spotify = SpotifyRequests;
    app.run(port=5500, debug=True)
