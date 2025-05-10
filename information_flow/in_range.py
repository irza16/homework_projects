"""Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) 

 Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("Enter n: "))
    low = int(input("Enter low value: "))
    high = int(input("Enter high value: "))
    print(in_range(n,low, high))

if __name__ == '__main__':
    main()
