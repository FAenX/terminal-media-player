import os
from files import FileFunctions


#  ensure playlist.txt and pre-playlist.txt exists
def checkPlaylistFilesExists(path):    
    files = os.listdir(os.path.curdir)

    if 'pre-playlist.txt' in os.listdir(os.path.curdir):
        os.rename('pre-playlist.txt', 'playlist.txt')

    else: 
        musicDir = path  
        fileFunctions = FileFunctions(musicDir)
        with open('playlist.txt', 'w') as playlist:
            #pick random song
            try:
                playlist.write(fileFunctions.findRandomSong())
            except Exception as e:
                raise e
   
    player = os.execl('./player.sh', 'bash' )
    return 0




