"""Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

# import random

# def main():
#     num = random.randint(0, 99)
#     print("I am thinking of a number between 0 and 99...")
#     while True:  
         
#          guess = int(input("Enter a guess: "))
    
#          if guess > num:
#             print("Your guess is too high")
            
#          elif num > guess:
#                 print("Your guess is too low")
                
#          else: 
#                 print("Congrats! The number was: ", num)
#                 break


# if __name__ == '__main__':
#      main()

#OR

import random

def main():
    secret_num = random.randint(0,99)
    print("I am thinking of a number between 0 and 99...")

    guess = int(input("Enter a guess: "))

    while guess != secret_num:
        if guess > secret_num:
            print("Your guess is too high.")

        else: 
            print("Your guess is too low.")

        print()

        guess = int(input("Enter a new guess: "))

        print("Congrats! The number was: " + str(secret_num))
    
if __name__ == '__main__':
    main()



     


