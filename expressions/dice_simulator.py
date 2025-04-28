# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random #this library is imported to generate random numbers for dice / used to simulate rolling dice

num_sides = 6 #global variable to store number of sides on each dice to roll

def roll_dice():

    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    total: int = die1 + die2
    print("Total of two dice is", total)

def main():
    
    die1: int = 10
    print('die1 in main() starts as: ' + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()
