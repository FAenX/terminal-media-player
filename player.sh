#!/bin/bash

mpv --playlist=playlist.txt | exit
mv playlist.txt cached-playlist.txt 
mv pre-playlist.txt playlist.txt | exit



