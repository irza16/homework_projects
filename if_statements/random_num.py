"""Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92

Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:"""

import random

def main():
    for num in range(10):
        num = random.randint(1,100)
        print(num, end=" ") #this end prints the numbers on the same line 

if __name__ == '__main__':
    main()
