def create_Loc_P_tuple(Location,Playlist):
    if location is not None and Playlist is not None:
     location_playlist_tuple = (Location, Playlist)
     return location_playlist_tuple
    else:
      return None


# location and playlist need to be accepted seperately 
# after this you can compare added Loc values to this tuple