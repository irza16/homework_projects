"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random

num_sides:int = 6

def main():
    die1:int = random.randint(1, num_sides)
    die2:int = random.randint(1, num_sides)

    total:int = die1 + die2

    print("Dice has",num_sides, "each")
    print("First Die:", die1)
    print("Second Die:", die2)
    print("Total of two die:", total)

if __name__ == "__main__":
    main()


