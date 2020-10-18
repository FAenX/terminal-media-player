#!/bin/bash

function play() {
    mpv --playlist=playlist.txt || exit
    cat playlist.txt >> cached-playlist.txt 
    rm playlist.txt 
    mv pre-playlist.txt playlist.txt || exit
}

# loop
while true; 
do play;
done;


    
