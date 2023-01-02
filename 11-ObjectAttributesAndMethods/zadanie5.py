class music():
    def __init__(self, artist, song, album, year):
       self.artist = artist
       self.song = song
       self.album = album
       self.year = year
    def __str__(self):
        return f"Performer: {self.artist}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

m = music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
print(m)