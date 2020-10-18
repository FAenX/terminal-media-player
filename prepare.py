import os
import sys
from files import FileFunctions

files = os.listdir(os.path.curdir)

#  ensure playlist.txt and pre-playlist.txt exists
def prepare_folder(path):    
    musicDir = path  
    l_files = FileFunctions(musicDir).getSongList()
    with open('playlist.txt', 'w') as playlist:
        for file in l_files:
            playlist.write(file + '\n')
        # launch player
    launch_player()

def single_song(path):
    with open('playlist.txt', 'w') as playlist:       
        playlist.write(path)
        # launch player
    launch_player()

def cached():
    if 'cached-playlist.txt' in files:
        os.rename('cached-playlist.txt', 'playlist.txt')
        launch_player()
    else:
        print('no cached playlist')
        sys.exit()       


def launch_player():
    return os.execl('./player.sh', 'bash' )




