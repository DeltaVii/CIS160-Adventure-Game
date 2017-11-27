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
    return input("What will you do? ")

#The Rooms are list objects that have 5 elements:
#The first element is a multi-line string that describes the room.
#The next 4 elements describe the layout of the "dungeon"
#They are the integers of the room numbers in whatever direction
    #they're in relative to the room.
#The order is N, E, S, W for elements 1, 2, 3 and 4.
#For example, room #0 has room #5 to the north and room #3 to the east.
#It's list would be ['''(descriptor)''', 5, 3, None, None]
room_list = []

#room 0: Slate
room = ["""A white, blank slate surrounds you.
The only thing you can see is a door off to the north.
You don't really know how you can tell what north is.
But you're gonna assume the door is north and roll with it.""", 1, None, 2, None]
room_list.append(room)

#room 1: The Door
room = ["""A large, ornate wooden door stands at your "north" side.
It doesn't seem to be attatched to anything else, and there's nothing behind it.
It has a metal lock above the handle.""", 3, None, 0, None]
room_list.append(room)

#room 2: Void
#On the first visit to this room, a key can be found.
room = ["""You've walked farther away from the door.
Yep. Nothing but white forever in all directions but that door.""", 0, None, None, None]
room_list.append(room)

#room 3: Grove
room = ["""You stand in a small, lush grove.
The grove is sourrounded by plant life and trees.
You can hear a stream running in the distance.
To the east is a small trail of grass.""", None, 4, None, None]
room_list.append(room)

#room 4: Man
room = ["""A black figure sits in another small clearing.
The sound of the stream has gotten slightly louder.
Something about this place calms and collects your mind.""", None, None, None, 3]
room_list.append(room)


## Lock System ##
#Some directions can have "locks"
#If the lock cannot be bypassed yet, it is "True"
#If the lock has been bypassed, it is "False"
#a "Key" variable is considered an item, so until the player has it, it is "False"
#Once the player obtains the item, it is set to "True"
#Locks are 'logic' variables.
#There can be many 'logic' variables, like first room visits or other interactions.
door_lock = True
door_key = False

#First Visit variables
#more 'logic' variables
#A room not visited that has an associated event has a "True" first variable.
slate_first = True
void_first = True
man_first = True


#Room variables
next_room = None
current_room = 0


#loop variable
done = False

#game loop
while done != True:

    #First Room Visit Events
    if current_room == 0 and slate_first == True:
        slate_first = False
        print("You come into existance, with no memory of what you were.")

    if current_room == 2 and void_first == True:
        void_first = False
        print("You find a key on the ground.")
        print()
        door_key = True

    if current_room == 4 and man_first == True:
        man_first = False
        print("The figure says hello.")
        print()

    #Checking for Locked Doors
    if current_room == 3 and door_lock == True and door_key == False:
        print("The door is locked.")
        print()
        current_room = 1
        
    if current_room == 3 and door_lock == True and door_key == True:
        print("You unlock the door.")
        print()
        door_lock = False

    #Room descriptor printer
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
    print()
    
    #Direction input
    print("Will you go in a direction? n, e, s, w?")
    go = get_input()
    print()
  
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


        
