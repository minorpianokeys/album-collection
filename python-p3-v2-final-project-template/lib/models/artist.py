from models.__init__ import CURSOR, CONN

class Artist:

    all = {}

    def __init__(self, name, genre, id=None):
        self.id = id
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f"Artist {self.id} - {self.name}"
    
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
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO artists (name, genre)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.genre))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, genre):
        artist = cls(name, genre)
        artist.save()
        return artist
    
    def update(self):
        sql = """
            UPDATE artists
            SET name = ?, genre = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.genre, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
            artist.genre = row[2]
        else:
            artist = cls(row[1], row[2])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM artists
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] 
    
    def albums(self):
        from models.album import Album
        sql = """
            SELECT *
            FROM albums
            WHERE artist_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Album.instance_from_db(row) for row in rows]