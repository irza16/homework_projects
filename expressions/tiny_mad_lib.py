"""Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
"""

start_sent:str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective:str = input("Please enter a adjective and press enter. ")
    noun:str = input("Please enter a noun and press enter. ")
    verb:str = input("Please enter an verb and press enter. ")

    print(start_sent + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()
