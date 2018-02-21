import math
import re
from Classes import Classes

def Diskriminant(value1, value2, value3):
    RESULT = (value2**2) - (4 * value1 * value3)
    if RESULT > 0:
        print("Jsou 2 řešení. Hodnota diskriminantu je: ", RESULT)
    elif RESULT == 0:
        print("Je 1 řešení. Hodnota diskriminantu je: ", RESULT)
    else:
        print("Není řešení. Hodnota diskriminantu je: ", RESULT)

def GetDivisable(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)
    return divisors

# 1. Převod úhlů na radiány
Classes.UserInterface.PrintHeader("1", "Převod úhlů na radiány", True)
ANGLE = input("Zadejte úhel: ")

try:
    ANGLE = float(ANGLE)
    RADIAN = ANGLE * (math.pi/180)
    print(RADIAN, "rad")
except ValueError:
    print("Wrong value...")

# 2. Převod radiánů na úhly
Classes.UserInterface.PrintHeader("2", "Převod radiánů na úhly", False)
try:
    RADIAN = float(input("Zadejte radiány: "))
    ANGLE = RADIAN * (180/math.pi)
    print("Úhel: ", ANGLE)
except ValueError:
    print("Wrong value...")

# 3. Plocha lichoběžníku
Classes.UserInterface.PrintHeader("3", "Plocha lichoběžníku", False)
try:
    HEIGHT = float(input("Zadejte výšku: "))
    BASE1 = float(input("Zadejte první základnu: "))
    BASE2 = float(input("Zadejte druhou základnu: "))
    PLOCHA = ((BASE1 + BASE2) / 2) * HEIGHT
    print("Plocha lichoběžníku je: ", PLOCHA)
except ValueError:
    print("Wrong value...")

# 4. Diskriminant
# Viz. metoda Diskriminant na řádku 5
Classes.UserInterface.PrintHeader("4", "Diskriminant", False)
try:
    VALUE1 = float(input("Hodnota a: "))
    VALUE2 = float(input("Hodnota b: "))
    VALUE3 = float(input("Hodnota c: "))
    Diskriminant(VALUE1, VALUE2, VALUE3)
except ValueError:
    print("Wrong value...")

# 5. Výpis dělitelných čísel
# Viz. metoda Diskriminant na řádku 14
Classes.UserInterface.PrintHeader("5", "Výpis dělitelných čísel", False)
print(GetDivisable(100))

Classes.UserInterface.PrintEnd()