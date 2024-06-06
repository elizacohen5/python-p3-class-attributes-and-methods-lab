class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increase_song_count()
        self.add_to_genres(self)
        self.add_to_artists(self)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)
    
    @classmethod
    def increase_song_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
    
    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
    
    @classmethod
    def add_to_genre_count(cls, self):
        if self.genre in cls.genre_count:
            cls.genre_count[self.genre] += 1
        else:
            cls.genre_count[self.genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, self):
        if self.artist in cls.artist_count:
            cls.artist_count[self.artist] += 1
        else:
            cls.artist_count[self.artist] = 1



    
baby = Song('baby', 'justin beiber', 'pop')
judas = Song('judas', 'lady gaga', 'pop')
back_in_black = Song('back in black', 'acdc', 'rock')

print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)


        
        
