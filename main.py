import os
import argparse
from prepare import prepare_folder, single_song, cached
import sys
from files import FileFunctions


def parseArgs():
    # create a parser
    parser = argparse.ArgumentParser(description='Termianl wrapper fro mpv player')
    parser.add_argument("-p", "--path", help="path to music/ music directory")
    parser.add_argument("-s", "--search", help="search text")
    parser.add_argument("--resume", action='store_true', help="resume from cached playlist")
    args = parser.parse_args()
    return args

# run code
if __name__ == '__main__':
    args = parseArgs()
    print(args)

    if args.path == None and args.search == None and args.resume == None:
        print('type -h for help')
        sys.exit()

    elif args.search and args.path:
        songs = FileFunctions(args.path).getSongList()
        found = [file for file in songs if args.search in file]
        for i in found:
            print(i)

    elif args.path and os.path.isdir(args.path) == True:
        prepare_folder(args.path)

    elif args.path and os.path.isfile(args.path) == True:
        single_song(args.path)

    elif args.resume:
        cached()

    else:
        print('type -h for help')

    


    
    
   

    
    

    