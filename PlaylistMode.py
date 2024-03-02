import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, Toplevel


# Spotify client setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="069f73ab59bd4d859710fcc0c2be86a2",
                                               client_secret="9280fe9224384285ad44c1f3c85e460f",
                                               redirect_uri="http://127.0.0.1:5000/redirect",
                                               scope="streaming, playlist-read-private,  user-modify-playback-state"))

# Global list to keep track of modes
modes = []

# Function to fetch user playlists
def fetch_user_playlists():
    playlists = sp.current_user_playlists()
    playlist_names = [playlist['name'] for playlist in playlists['items']]
    playlist_ids = [playlist['id'] for playlist in playlists['items']]
    return playlist_names, playlist_ids

# Function to create a new mode
def create_new_mode():
    mode_name = simpledialog.askstring("New Mode", "Enter the name of the new mode:")
    if mode_name:
        open_customize_window(mode_name)

# Function to open the customize window
def open_customize_window(mode_name):
    customize_window = Toplevel(window)
    customize_window.title(f"Customize {mode_name}")

    tk.Label(customize_window, text=f"Select a playlist for {mode_name}:").pack()

    playlists, playlist_ids = fetch_user_playlists()
    playlist_var = tk.StringVar(customize_window)
    playlist_var.set(playlists[0])  # default value

    playlist_dropdown = tk.OptionMenu(customize_window, playlist_var, *playlists)
    playlist_dropdown.pack()

    save_button = tk.Button(customize_window, text="Save", command=lambda: save_mode(mode_name, playlist_var.get(), playlist_ids[playlists.index(playlist_var.get())]))
    save_button.pack()

# Function to save a mode and update the list
def save_mode(mode_name, playlist_name, playlist_id):
    modes.append({'name': mode_name, 'playlist': playlist_name, 'playlist_id': playlist_id})
    update_modes_display()

# Function to update the display of modes on the main window
def update_modes_display():
    mode_list.delete(0, tk.END)  # Clear the current list
    for mode in modes:
        mode_list.insert(tk.END, f"{mode['name']}: {mode['playlist']}")

# Function to handle mode selection from the listbox
def on_mode_select(event):
    # Get selected index
    index = mode_list.curselection()
    if index:
        index = index[0]  # Get the first item in the tuple
        mode = modes[index]  # Fetch the mode from the global modes list
        play_playlist(mode['playlist_id'])  # Play the playlist

# Function to play the selected playlist
def play_playlist(playlist_id):
    # Construct the playlist URI
    playlist_uri = f'spotify:playlist:{playlist_id}'
    # Use Spotipy to start playback
    try:
        sp.start_playback(context_uri=playlist_uri)
        print(f"Playing playlist: {playlist_uri}")
    except Exception as e:
        print(f"Error playing playlist: {e}")

# Main application window
window = tk.Tk()
window.title("Mode Player")

# Listbox to display modes
mode_list = tk.Listbox(window)
mode_list.pack(fill=tk.BOTH, expand=True)
mode_list.bind('<<ListboxSelect>>', on_mode_select)

# "+" button to add new mode
add_mode_button = tk.Button(window, text="+", command=create_new_mode)
add_mode_button.pack(anchor='ne')

window.mainloop()