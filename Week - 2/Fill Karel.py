from karel.stanfordkarel import *

def main():
    while left_is_clear():
          fill_the_row()
          reset_to_next_row()
    fill_the_row()
    
def fill_the_row():
    put_beeper()
    while front_is_clear():
          move()
          put_beeper()
          
def reset_to_next_row():
    turn_around()
    while front_is_clear():
          move()
    turn_right()
    move()
    turn_right()
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()