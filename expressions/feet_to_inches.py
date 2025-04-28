# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_IN_FOOT:int = 12 #conversion factor

def main():

    feet = float(input("Enter number of feets to convert into Inches: "))
    Inches = feet * INCHES_IN_FOOT
    print("feets:",feet, "Inches:", Inches)

if __name__ == '__main__':
    main()