#Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers) -> int:
    total_so_far:int = 0
    for number in numbers:
        total_so_far +=number
    return total_so_far

def main():
    # Take input as a string (e.g., "1 2 3 4 5")
    input_str = input("Enter numbers separated by spaces: ")

    # Split the string into a list of strings and convert to integers
    numbers = list(map(int, input_str.split()))

    print("List of numbers:", numbers)

    sum_of_numbers:int = add_many_numbers(numbers)
    print(sum_of_numbers)


if __name__ == '__main__':
    main()
