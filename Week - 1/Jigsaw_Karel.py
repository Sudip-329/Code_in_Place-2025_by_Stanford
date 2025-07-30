from karel.stanfordkarel import *

def main():
    move_to_and_pick_last_beeper()
    place_beeper_at_destination()
    return_to_starting_point()

def move_to_and_pick_last_beeper():
    while no_beepers_present():
        move()
    pick_beeper()

def place_beeper_at_destination():
    move()            
    turn_left()       
    move()
    move()            
    put_beeper()

def return_to_starting_point():
    turn_around()
    move()
    move()            
    turn_right()
    move()
    move()
    move()            
    face_east()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def face_east():
    while not_facing_east():
        turn_left()

if __name__ == '__main__':
    main()
