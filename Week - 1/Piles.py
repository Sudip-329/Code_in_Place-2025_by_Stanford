from karel.stanfordkarel import *

def main():
    move()
    pick_up_pile()

    move()
    move()
    pick_up_pile()

    move()
    move()
    pick_up_pile()
    
    move()

def pick_up_pile():
    for i in range(10):
        pick_beeper()

if __name__ == '__main__':
    main()