from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Album:

    all = {}

    def __init__(self, name, year, artist_id, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.artist_id = artist_id

    def __repr__(self):
        return f"{self.id} - {self.name}({self.year})"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(year, int) and 1900 <= year <= 2024:
            self._year = year
        else:
            raise ValueError("year must be an integer")
        
    @property
    def album_id(self):
        return self._album_id
    
    @album_id.setter
    def album_id(self, artist_id):
        if type(artist_id) is int and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError("album_id must reference a department in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            name TEXT,
            year INTEGER,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS albums;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO albums (name, year, artist_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.year, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, year, artist_id):
        album = cls(name, year, artist_id)
        album.save()
        return album
    
    def update(self):
        sql = """
            UPDATE albums
            SET name = ?, year = ?, artist_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.year, self.artist_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM albums
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        album = cls.all.get(row[0])
        if album:
            album.name = row[1]
            album.year = row[2]
            album.artist_id = row[3]
        else:
            album = cls(row[1], row[2], row[3])
            album.id = row[0]
            cls.all[album.id] = album
        return album