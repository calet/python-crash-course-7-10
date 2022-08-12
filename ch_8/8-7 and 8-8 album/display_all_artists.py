def all_artists(music_album):
    for artists, albums in music_album.items():
        if albums.values():
            for album, songs in albums.items():
                print(f"\nartist: {artists}")
                print(f"album: {album}")
                print(f"songs: {songs}")