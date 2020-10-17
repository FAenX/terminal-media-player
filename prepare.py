import os
from files import FileFunctions


#  ensure playlist.txt and pre-playlist.txt exists
def checkPlaylistFilesExists(path):    
    musicDir = path  
    fileFunctions = FileFunctions(musicDir)
    files = os.listdir(os.path.curdir)

    with open('playlist.txt', 'w') as playlist:
        #pick random song
        try:
            playlist.write(fileFunctions.findRandomSong())
        except Exception as e:
            raise e

   
    os.execl('./player.sh', 'bash' )
    

    return 0




