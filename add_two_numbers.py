"""Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message."""


def main():

    num1 = int(input("Enter first Number:"))

    num2 = int(input("Enter second number:"))

    sum = num1 + num2

    print("The sum of the numbers is:",sum)


if __name__ == '__main__':
    main()

