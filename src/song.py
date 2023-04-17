class Song:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        
    def equals(self,song):
        return song.name == self.name and song.genre == self.genre