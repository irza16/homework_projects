"""Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture."""

def subtract_seven(num):
    return num - 7

def main():
    num = int(input("Enter a number: "))
    sub_7 = subtract_seven(num)
    print("7 subtracted from", num, "is", sub_7)

if __name__ == '__main__':
    main()
