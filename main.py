#****************************************************************
# File:			main.py
# Description:  	Adventure Game
# Author: 		Kelly Norris and Sam Torris
# Date created: 	11/17/17
# Compiler:		Python 3.6.2
#****************************************************************
import time
import sys

def get_input():
    return input("What will you do?")

#The Rooms are list objects that have 5 elements:
#The first element is a multi-line string that describes the room.
#The next 4 elements describe the layout of the "dungeon"
#They are the integers of the room numbers in whatever direction
    #they're in relative to the room.
#The order is N, E, S, W for elements 1, 2, 3 and 4.
#For example, room #0 has room #5 to the north and room #3 to the east.
#It's list would be ['''(descriptor)''', 5, 3, None, None]
room_list = []

room = ["""This is a test room.
Room 0 will be replaced at some point.""", 1, None, None, None]
room_list.append(room)

room = ["""This is another test room.
Room 1 will be replaced at some point.""", None, None, 0, None]
room_list.append(room)


next_room = None
current_room = 0

done = False

while done != True:

    #Room descriptor printer
    print(room_list[current_room][0])
    for i in room_list[current_room][0]:
        if i == ".":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.5)
        elif i == ",":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    print()
    
    #Direction input
    print("Will you go in a direction? n, e, s, w?")
    go = get_input()
  
    #direction checks
    if go == "n" or go == "north" or go == "N" or go == "North":
        next_room = room_list[current_room][1]
    elif go == "e" or go == "east" or go == "E" or go == "East":
        next_room = room_list[current_room][2]
    elif go == "s" or go== "south" or go== "S" or go == "South":
        next_room = room_list[current_room][3]
    elif go == "w" or go == "west" or go== "W" or go == "West":
        next_room = room_list[current_room][4]

    #Moving next_room to current_room, checking if room is None
    if next_room != None:
        current_room = next_room
    else:
        print()
        if done == False:
            print("You cannot go that way.")
        print()


        
