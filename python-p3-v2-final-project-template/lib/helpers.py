# lib/helpers.py
from models.artist import Artist
from models.album import Album

def greet_user():
    print("********************************")
    print("Welcome to the Album Collection!")
    print("********************************")
    print("")
    print("Type A to see all artists")
    print("Type 0 to exit program")

def exit_program():
    print("Goodbye!")
    exit()

def list_all_artists():
    artists = Artist.get_all()
    for i, artist in enumerate(artists, start=1):
        print(f"{i} - {artist.name}({artist.genre})")

def list_albums(artist):
    albums = Artist.albums(artist)
    if albums:
        for i, album in enumerate(albums, start=1):
            print(f"{i} - {album.name}({album.year})")
    else:
        print("No albums for this artist")

def pick_artist(choice):
    artists = Artist.get_all()
    if 0 < int(choice) <= len(artists):
        artist = artists[int(choice) - 1]
        return artist
    else:
        print("No artist found")

def pick_album(artist, choice):
    albums = Artist.albums(artist)
    if 0 < int(choice) <= len(albums):
        album = albums[int(choice) - 1]
        return album
    else:
        print("No album found")

def create_artist():
    name = input("Enter artist's name: ")
    genre = input(f"Enter {name}'s genre: ")
    try:
        artist = Artist.create(name, genre)
        print(f'You have added {artist.name}')
        choice = input("Would you like to add an album to this artist? 'y' or 'n': ")
        if choice == "y":
            create_album(artist)
    except Exception as exc:
        print("Error creating artist ", exc)

def update_artist(artist):
    try:
        name = input("Enter the artist's new name or click <enter> to keep it the same: ")
        if name == "":
            artist.name = artist.name
        else:
            artist.name = name
        genre = input("Enter the artist's new genre or click <enter> to keep it the same: ")
        if genre == "":
            artist.genre = artist.genre
        else:
            artist.genre = genre

        artist.update()
        print(f"Success: {artist.name} updated")
    except Exception as exc:
        print("Error updating artist: ", exc)

def delete_artist(artist):
    choice = input(f"Are you sure you want to delete {artist.name} and their albums? 'y' or 'n': ")
    if choice == "y":
        albums = Artist.albums(artist)
        for album in albums:
            album.delete()
        artist.delete()
        print(f"{artist.name} deleted")

def create_album(artist):
    name = input("Enter album's name: ")
    year = int(input("Enter year album came out: "))
    try:
        Album.create(name, year, artist.id)
        print(f"You have added {name} to {artist.name}")
    except Exception as exc:
        print("Error creating album: ", exc)

def update_album(album):
    try:
        name = input("Enter the album's new name or click <enter> to keep it the same: ")
        if name == "":
            album.name = album.name
        else:
            album.name = name
        year = int(input("Enter the album's new year or click <enter> to keep it the same: "))
        if year == "":
            album.year = album.year
        else:
            album.year = year

        album.update()
        print(f"Success: {album.name} updated")
    except Exception as exc:
        print("Error updating album: ", exc)

def delete_album(album):
    choice = input(f"Are you sure you want to delete {album.name}? 'y' or 'n': ")
    if choice == "y":
        album.delete()
        print(f"{album.name} deleted")





    
