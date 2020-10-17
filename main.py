import os
import argparse
import prepare
import sys


def parseArgs():
    # create a parser
    parser = argparse.ArgumentParser(description='music path')
    parser.add_argument("-p", "--path", help="path to music folder")
    args = parser.parse_args()
    return args

# run code
if __name__ == '__main__':
    args = parseArgs()

    if args.path == None:
        print('type -h for help')
        sys.exit()

    if os.path.isdir(args.path) == False:
        print('type path/to/music')
        sys.exit()
    
    path = args.path
    path = os.path.abspath(path)

    prepare.checkPlaylistFilesExists(path)

    
    

    