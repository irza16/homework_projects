"""Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Here's a sample run (user input is in blue):

Enter a number: 42 The ones digit is 2

"""

def print_ones(num):
    return num % 10

def main():
    num = int(input("Enter a number: "))
    ones_digit = print_ones(num)
    print("The one's digit is:", ones_digit)

if __name__ == '__main__':
    main()
