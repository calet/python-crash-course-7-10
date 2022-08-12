import album 
from display_all_artists import all_artists as d_a_a

music_album = {}
more_songs = []
    
flag = True
while flag:
    print("\n-create album-")
    print("(write 1 to exit)")
    print("(write 2 to show all artists/albums)")
    
    first_name = input("\nwrite first name of artist: ")
    
    if first_name == '1':
        flag = False
    elif first_name == '2':
        if music_album:
            d_a_a(music_album)
        else:
            print("\n--no artists/albums--")

    else:
        artist_name = first_name
        while flag:
            last_name = input("write last name of artist: ")
            if last_name == '1':
                flag = False
            elif last_name == '2':
                if music_album:
                    d_a_a(music_album)
                    print(f"pending artist: {artist_name}\n")
                else:
                    print("\n--no artists/albums found--")
                    print(f"pending artist: {artist_name}\n")
            else:
                artist_name += ' ' + last_name
                break
        while flag:
            album_name = input("write album name: ")
            if album_name == '1':
                flag = False
            elif album_name == '2':
                if music_album:
                    d_a_a(music_album)
                    print(f"\npending artist: {artist_name}\n")
                else:
                    print("\n--no artists/albums found--")
                    print(f"pending artist: {artist_name}\n")
            else:
                break
        while flag:
            song_name = input("write song name: ")
            if song_name == '1':
                flag = False
            elif song_name == '2':
                if music_album:
                    d_a_a(music_album)
                    print(f"\npending artist:")
                    print(artist_name)
                    print(album_name)
                else:
                    print("\n--no artists/albums found--")
                    print(f"\npending artist:")
                    print(artist_name)
                    print(album_name)
            else:
                choice = input("\ndo you want more songs added to album? y/n: ")
                print("")
                if choice == 'y':
                    more_songs.append(song_name)
                else:
                    if more_songs:
                        more_songs.append(song_name)
                    album.make_album(artist_name, album_name, song_name, more_songs, music_album)
                    break
#add more albums
'''
if a written album then let the user input if they want another album or not:
if they want to then the computer go back to "write a album" function so they can write another one,
they are asked to add another album after they written all the songs for current album,
the current album and its songs is then stored in a dictonary before the user can write another album and songs.
    
if the user doesnt want to write another album the program just add the current album into the dictonary and loop through everything again  
'''

#choose artist to add more songs and albums on
'''
inside the all_artist function ask the user which one they want to select through search function, 
if no artist/album/song that the user search for excist then tell the user it doesnt excist and loop back again,
if artist/album/song excist it will show the whole key/value pair for that album (if only first name show all first names of that name, or last name)
'''

#make a personal spotify (another program)

#GUI main
'''
when no artists/albums:
 -create album-
(write 1 to exit)
(write 2 to add artist)

when artists/albums:
 -create album-
(write 1 to exit)
(write 2 to add artist) #runs whole program as normal
(write 3 to show all artists/albums/songs)
'''

# GUI all artsts/albums/songs
#ex.
'''
-all albums-

Artist: 
-Johan

Album: 
-Christmas songs

Songs: 
-rudolph
-bjälleklang

.
.
.

search artist (first or last name)/album/song: johan

Artist: 
-Johan

Album: 
-Christmas songs

Songs: 
-rudolph
-bjälleklang

add album/song? (write a or s): 
#calls the related function
'''