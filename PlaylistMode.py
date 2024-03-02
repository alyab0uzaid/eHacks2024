import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, Toplevel


# Spotify client setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="069f73ab59bd4d859710fcc0c2be86a2",
                                               client_secret="9280fe9224384285ad44c1f3c85e460f",
                                               redirect_uri="http://127.0.0.1:5000/redirect",
                                               scope="streaming"))

# Global list to keep track of modes
modes = []

# Function to fetch user playlists
def fetch_user_playlists():
    playlists = sp.current_user_playlists()
    playlist_names = [playlist['name'] for playlist in playlists['items']]
    return playlist_names

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

    playlists = fetch_user_playlists()
    playlist_var = tk.StringVar(customize_window)
    playlist_var.set(playlists[0])

    playlist_dropdown = tk.OptionMenu(customize_window, playlist_var, *playlists)
    playlist_dropdown.pack()

    save_button = tk.Button(customize_window, text="Save", command=lambda: save_mode(mode_name, playlist_var.get()))
    save_button.pack()

# Function to save a mode and update the list
def save_mode(mode_name, playlist_name):
    modes.append({'name': mode_name, 'playlist': playlist_name})
    print(f"Mode '{mode_name}' is set to use the playlist '{playlist_name}'.")
    update_modes_display()

# Function to update the display of modes on the main window
def update_modes_display():
    mode_list.delete(0, tk.END)  # Clear the current list
    for mode in modes:
        mode_list.insert(tk.END, f"{mode['name']}: {mode['playlist']}")

# Main application window
window = tk.Tk()
window.title("Mode Player")

# Listbox to display modes
mode_list = tk.Listbox(window)
mode_list.pack(fill=tk.BOTH, expand=True)

# "+" button to add new mode
add_mode_button = tk.Button(window, text="+", command=create_new_mode)
add_mode_button.pack(anchor='ne')

window.mainloop()