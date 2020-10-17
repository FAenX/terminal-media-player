import os 
from random import randint


class FileFunctions:
    def __init__(self, path):
        self.path = path
        self.dirs = os.walk(self.path)
        

    def findRandomSong(self):
        songs = self.getSongList()
       
        start = 0
        end = int(len(songs))-1
        try:
            semiRandom = randint(start, end)
            return songs[semiRandom]
        except Exception as e:
            raise e
      

    def getSongList(self):
        songs=[]
        
        while True:
            try:
                d = self.dirs.__next__()   
                for file in d[2]:         
                    songs.append(os.path.join(d[0], file))   
            except:
                break  

        if len(songs) < 1:
            raise Exception('No songs')
            
        
        return songs


