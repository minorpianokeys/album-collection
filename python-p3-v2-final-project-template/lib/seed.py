from models.artist import Artist
from models.album import Album

def seed_database():
    Artist.drop_table()
    Album.drop_table()
    Artist.create_table()
    Album.create_table()

    chappell_roan = Artist.create("Chappell Roan", "Pop")
    lady_gaga = Artist.create("Lady Gaga", "Pop")
    my_chemical_romance = Artist.create("My Chemical Romance", "Rock")
    taylor_swift = Artist.create("Taylor Swift", "Pop")
    # ariana_grande = Artist.create("Ariana Grande", "Pop")
    # muna = Artist.create("Muna", "Indie")
    # the_beatles = Artist.create("The Beatles", "Rock")

    Album.create("The Rise and Fall of a Midwest Princess", 2023, chappell_roan.id)

    Album.create("The Fame", 2007, lady_gaga.id)
    Album.create("The Fame Monster", 2009, lady_gaga.id)
    Album.create("Born This Way", 2010, lady_gaga.id)
    Album.create("ARTPOP", 2013, lady_gaga.id)
    Album.create("Joanne", 2016, lady_gaga.id)
    Album.create("Chromatica", 2020, lady_gaga.id)

    Album.create("I Brought You Bullets, You Brought Me Your Love", 2001, my_chemical_romance.id)
    Album.create("Three Cheers for Sweet Revenge", 2004, my_chemical_romance.id)
    Album.create("The Black Parade", 2006, my_chemical_romance.id)
    Album.create("Danger Days", 2010, my_chemical_romance.id)
    Album.create("May Death Never Stop You", 2014, my_chemical_romance.id)

    Album.create("Taylor Swift", 2006, taylor_swift.id)
    Album.create("Fearless", 2008, taylor_swift.id)
    Album.create("Speak Now", 2010, taylor_swift.id)
    Album.create("Red", 2012, taylor_swift.id)
    Album.create("1989", 2014, taylor_swift.id)
    Album.create("reputation", 2017, taylor_swift.id)
    Album.create("Lover", 2019, taylor_swift.id)
    Album.create("Folklore", 2020, taylor_swift.id)
    Album.create("Evermore", 2020, taylor_swift.id)
    Album.create("Midnights", 2022, taylor_swift.id)
    Album.create("THE TORTURED POETS DEPARTMENT", 2024, taylor_swift.id)

seed_database()
print("Seeded database")