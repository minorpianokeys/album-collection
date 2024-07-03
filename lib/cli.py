# lib/cli.py
from models.artist import Artist
from models.album import Album

from helpers import (
    create_artist,
    list_all_artists,
    list_albums,
    update_artist,
    delete_artist,
    pick_artist,
    pick_album,
    create_album,
    update_album,
    delete_album,
    greet_user,
    exit_program
)


def main():
    while True:
        greet_user()
        choice = input("> ")
        if choice == "A" or choice == "a":
            artists_loop()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def artists_loop():
    while True:
        artist_menu()
        choice = input("> ")
        if choice == "N" or choice == "n":
            create_artist()
        elif choice == "U" or choice == "u":
            update_artist()
        elif choice == "B" or choice == "b":
            main()
        elif choice == "0":
            exit_program()
        elif choice.isdigit():
            artist = pick_artist(choice)
            if artist:
                albums_loop(artist)
        else:
            print("Invalid choice")


def albums_loop(artist):
    while True:
        albums_menu(artist)
        choice = input("> ")
        if choice == "N" or choice == "n":
            create_album(artist)
        if choice == "U" or choice == "u":
            update_artist(artist)
        elif choice == "D" or choice == "d":
            delete_artist(artist)
            artists_loop()
        elif choice == "B" or choice == "b":
            artists_loop()
        elif choice == "0":
            exit_program()
        elif choice.isdigit():
            album = pick_album(artist, choice)
            if album:
                album_info_loop(album, artist)
        else:
            print("Invalid choice")

def album_info_loop(album, artist):
    while True:
        album_menu(album, artist)
        choice = input("> ")
        if choice == "U" or choice == "u":
            update_album(album)
        elif choice == "D" or choice == "d":
            delete_album(album)
            albums_loop(artist)
        elif choice == "B" or choice == "b":
            albums_loop(artist)
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def artist_menu():
    print("Your Artists:")
    print("----------------------------")
    print("")
    list_all_artists()
    print("")
    print("----------------------------")
    print("Please select the number of the artist to see their albums/options")
    print("")
    print("Type N to add a new artist")
    print("Type B to go back to the home page")
    print("Type 0 to exit the program")

def albums_menu(artist):
    print(f"{artist.name}'s albums:")
    print("----------------------------")
    print("")
    list_albums(artist)
    print("")
    print("----------------------------")
    print("Please select the number of the album to see more info/options")
    print("")
    print(f"Type N to add a new album to {artist.name}")
    print(f"Type U to update {artist.name}")
    print(f"Type D to delete {artist.name}")
    print("Type B to go back to the all artists")
    print("Type 0 to exit the program")

def album_menu(album, artist):
    print("----------------------------")
    print("")
    print(f"Name: {album.name}")
    print(f"Year: {album.year}")
    print("")
    print("----------------------------")
    print(f"Type U to update {album.name}")
    print(f"Type D to delete {album.name}")
    print(f"Type B to go back to {artist.name}'s albums")
    print("Type 0 to exit the program")

if __name__ == "__main__":
    main()
