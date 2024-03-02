import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk

# Spotify client setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="069f73ab59bd4d859710fcc0c2be86a2",
                                               client_secret="9280fe9224384285ad44c1f3c85e460f",
                                               redirect_uri="http://127.0.0.1:5000/redirect",
                                               scope="streaming"))

def test_spotify_api():
    # Fetch the current user's profile
    user_info = sp.current_user()
    # Print the display name of the user
    print(f"Successfully authenticated as: {user_info['display_name']}")

#implement code to decide on what music to play based on heart rate and location 
    
def play_study_playlist():
    # Logic to play study playlist
    pass

def play_gym_playlist():
    # Logic to play gym playlist
    pass
def play_school_playlist():
    #logic to play school playlist 
    pass

# Test the Spotify API connection
test_spotify_api()

# GUI setup
window = tk.Tk()
window.title("Mode Player")

study_button = tk.Button(window, text="Study Mode", 
command=play_study_playlist)
study_button.pack()

gym_button = tk.Button(window, text="Gym Mode", command=play_gym_playlist)
gym_button.pack()

school_button = tk.Button(window, text="School Mode", 
command=play_school_playlist)
school_button.pack()

window.mainloop()
