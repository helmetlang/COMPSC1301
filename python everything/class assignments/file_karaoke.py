
name_of_song = input("What song file do you want to sing? ")

song = open(name_of_song, "r+") # read+
title = song.readline()

print("Title: " + title)