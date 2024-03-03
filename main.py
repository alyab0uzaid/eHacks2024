
import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spotipy
from spotipy.oauth2 import SpotifyOAuth

App = FastAPI()

# Spotify client setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="069f73ab59bd4d859710fcc0c2be86a2",
                                               client_secret="9280fe9224384285ad44c1f3c85e460f",
                                               redirect_uri="http://127.0.0.1:5000/redirect",
                                               scope="streaming"))

# Global list to keep track of modes
modes = []

# Fetch user playlists

@App.get("/playlists")
async def fetch_user_playlists():
    playlists = sp.current_user_playlists()
    playlist_names = [playlist['name'] for playlist in playlists['items']]
    playlist_ids = [playlist['id'] for playlist in playlists['items']]
    return{"playlist_names": playlist_names, "playlist_ids": playlist_ids}

# Play a playlist
@App.get("/play/{playlist_id}")
async def play_playlist(playlist_id: str):
    playlist_uri = f'spotify:playlist:{playlist_id}'
    try:
        sp.start_playback(context_uri=playlist_uri)
        return {"message": f"Playing playlist: {playlist_uri}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

