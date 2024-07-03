# WELCOME to Album Collection
This program is a CLI for managing an album collection and their artists. Users can create, update, delete, and view artists and albums from the command line.



# lib/cli.py
This file includes the navigational menus for the CLI. Users can navigate between artists and their albums as well as a welcome page. While loops control which menus the user is currently in by keeping them in that menu until they select an options that sends them to a different while loop(menu).



# lib/helpers.py
This file includes helper functions that work with lib/cli.py to help create the front-end for the user. The functions interact with the Artist and Album models, facilitating user interactions and CRUD (Create, Read, Update, Delete) operations within the CLI.

## Functions
- **greet_user()**: Displays the home page to the user.
- **exit_program()**: Exits the program.
- **list_all_artists()**: Lists all artists in database in an ordered list.
- **list_albums(artist)**: Lists all albums associated to a certain artist in database in an ordered list.
- **pick_artist(choice)**: Checks if the number the user chooses matches a number on the display. It will then return the correct artist the user selected.
- **pick_artist(artist, choice)**: Checks if the number the user chooses matches a number on the display. It will then return the correct album the user selected.
- **create_artist(artist)**: Creates a new artist.
- **update_artist(artist)**: Updates an artist.
- **delete_artist(artist)**: Deletes an artist.
- **create_album(artist)**: Creates a new album for a specific artist.
- **update_album(album)**: Updates an album.
- **delete_album(album)**: Deletes an album.



# lib/album.py
This file defines the Album class. This class has functions which create, read, update, and delete albums in the database. It also includes property methods to add appropriate constraints to the Album class.

## Functions
- **create_table(cls)**: Create the `albums` table in the database if it does not exist.
- **drop_table(cls)**: Drop the `albums` table from the database.
- **save(self)**: Saves any changes made to the `Album` class to the `albums` database.
- **create(cls, name, year, artist_id)**: Create and save a new album record in the database.
- **update(self)**: Update an existing album record in the database.
- **delete(self)**: Delete an album record from the database.
- **instance_from_db(cls, row)**: Create an album instance from a database row.
- **Property Validations**: Validate and manage the `name`, `year`, and `artist_id` properties.


# lib/artist.py
This file defines the Artist class. This class has functions which create, read, update, and delete artists in the database. It also includes property methods to add appropriate constraints to the Artist class.

## Functions
- **create_table(cls)**: Create the `artists` table in the database if it does not exist.
- **drop_table(cls)**: Drop the `artists` table from the database.
- **save(self)**: Saves any changes made to the `Artist` class to the `artists` database.
- **create(cls, name, genre)**: Create and save a new artist record in the database.
- **update(self)**: Update an existing artist record in the database.
- **delete(self)**: Delete an artist record from the database.
- **instance_from_db(cls, row)**: Create an artist instance from a database row.
- **get_all(cls)**: Retrieve all artist records from the database.
- **albums(self)**: List all albums associated with a specific artist.
- **Property Validations**: Validate and manage the `name`, and `genre` properties.