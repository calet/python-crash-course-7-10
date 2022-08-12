def make_album(name, album, songs, more_songs, music_album):
    if more_songs:
        songs = ', '.join(more_songs)

    music_album[name] = {}
    music_album[name][album] = songs