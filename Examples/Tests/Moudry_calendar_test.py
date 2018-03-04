import datetime
from datetime import date, timedelta, datetime
import calendar
import time
import math
from fractions import Fraction

TODAY = datetime.now()

#1
MONDAYS = 0
print("1)")
for YEAR in range(2018, 2019):
    for MONTH in range(1,13):
        if datetime(YEAR, MONTH, 1).weekday() == 0:
            MONDAYS = MONDAYS + 1
print("Number of mondays: ", MONDAYS)

#2
print("\n2)")
print(TODAY)
print(TODAY + timedelta(days=30))
print(TODAY - timedelta(days=30))

#3
print("\n3)")
try:
    SIDES = int(input("Number of sides: "))
    SIDELENGTH = int(input("Length of a side: "))
    PART1 = SIDES*(SIDELENGTH**2)
    PART2 = 4*math.tan(float(math.pi/SIDES))
    print("Result: ", PART1 / PART2)
except ValueError:
    print("Wrong input...")

#4
try:
    print("\n4)")
    NUMBER1 = int(input("Number 1: "))
    NUMBER2 = int(input("Number 2: "))
    NUMBER3 = int(input("Number 3: "))
    NUMBER4 = int(input("Number 4: "))
    if NUMBER2 > 0 and NUMBER4 > 0:
        print(NUMBER1, "/", NUMBER2, "+", NUMBER3, "/", NUMBER4, "=", Fraction(NUMBER1, NUMBER2) + Fraction(NUMBER3, NUMBER4))
        print(NUMBER1, "/", NUMBER2, "-", NUMBER3, "/", NUMBER4, "=", Fraction(NUMBER1, NUMBER2) - Fraction(NUMBER3, NUMBER4))
        print(NUMBER1, "/", NUMBER2, "*", NUMBER3, "/", NUMBER4, "=", Fraction(NUMBER1, NUMBER2) * Fraction(NUMBER3, NUMBER4))
        print(NUMBER1, "/", NUMBER2, "/", NUMBER3, "/", NUMBER4, "=", Fraction(NUMBER1, NUMBER2) / Fraction(NUMBER3, NUMBER4))
    else:
        print("Can't devide by zero...")
except ValueError:
    print("Wrong input...")