"""This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times."""


def get_user_nums():

    user_nums = []
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break

        num = int(user_input)
        user_nums.append(num)

    return user_nums

def count_nums(numbers):

    num_dict = {}
    for num in numbers:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():

    user_numbers = get_user_nums()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()