import os
import argparse
import prepare
import sys
from files import FileFunctions


def parseArgs():
    # create a parser
    parser = argparse.ArgumentParser(description='Termianl music player')
    parser.add_argument("-p", "--path", help="path to music folder")
    parser.add_argument("-s", "--search", help="search text")
    parser.add_argument("-a", "--add", help="add to playlist")
    parser.add_argument("-c", "--cont", help="play from created playlist")
    args = parser.parse_args()
    return args

# run code
if __name__ == '__main__':
    args = parseArgs()

    if args.path == None and args.search == None and args.add == None and args.cont == None:
        print('type -h for help')
        sys.exit()

    elif args.search and args.path:
        songs = FileFunctions(args.path).getSongList()
        found = [file for file in songs if args.search in file]
        for i in found:
            print(i)

    elif args.path and os.path.isdir(args.path) == True:
        path = args.path
        path = os.path.abspath(path)
        prepare.checkPlaylistFilesExists(path)

    elif args.add and os.path.isfile(args.add) == True:
        if 'pre-playlist.txt' in os.listdir(os.path.curdir):
            with open('pre-playlist.txt', 'a') as playlist:
                playlist.write(args.add)
        else:
            with open('pre-playlist.txt', 'w') as playlist:
                playlist.write(args.add)

    elif args.add and os.path.isdir(args.add) == True:
        if 'pre-playlist.txt' in os.listdir(os.path.curdir):
            with open('pre-playlist.txt', 'a') as playlist:
                playlist.write(args.add)
        else:
            with open('pre-playlist.txt', 'w') as playlist:
                playlist.write(args.add)

    elif args.cont:
        prepare.checkPlaylistFilesExists('')

    else:
        print('type -h for help')

    


    
    
   

    
    

    