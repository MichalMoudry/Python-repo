import datetime
from datetime import date, timedelta
import calendar
import time
from Classes import Classes

# 1. Časové razítko
Classes.UserInterface.PrintHeader("1", "Časové razítko", True)
TIMESTAMP = datetime.datetime.fromtimestamp(int("1284105682"))
print(TIMESTAMP)

# 2. Přestupný rok
Classes.UserInterface.PrintHeader("2", "Přestupný rok", False)
def IsLeapYear(YEAR):
    YEAR = "{year}".format(year=YEAR)
    NUMCHECK = YEAR.isdigit()
    if NUMCHECK:
        YEAR = int(YEAR)
        if YEAR % 4 == 0:
            return True
        else:
            return False
    else:
        return False

print(IsLeapYear(2016))

# 3. Převod data na den roku
Classes.UserInterface.PrintHeader("3", "Převod data na den roku", False)
TODAY = datetime.datetime.now()
DAY_OF_THE_YEAR = (TODAY - datetime.datetime(TODAY.year, 1, 1)).days + 1
print(DAY_OF_THE_YEAR)

# 4. Číslo týden z data
Classes.UserInterface.PrintHeader("4", "Číslo týden z data", False)
print(TODAY.isocalendar()[1])

# 5. Rozdíl mezi daty
# Požadované: třída date viz. line 2
Classes.UserInterface.PrintHeader("5", "Rozdíl mezi daty", False)
LASTWEEK = datetime.datetime(TODAY.year, TODAY.month, (TODAY.day - 7))
print(TODAY - LASTWEEK)

# 6. Poslední den měsíce v zadaném roce
# Požadované: namespace calendar viz. line 3
Classes.UserInterface.PrintHeader("6", "Poslední den měsíce v zadaném roce", False)
USER_YEAR = input("Zadejte rok: ")
NUMCHECK = USER_YEAR.isdigit()
if NUMCHECK:
    USER_YEAR = int(USER_YEAR)
    print(calendar.monthrange(USER_YEAR, TODAY.month)[1])
else:
    print("Input error.")

# 7. Přídání měsíce k zadanému datu
# Požadované: třída timedelta viz. line 2
Classes.UserInterface.PrintHeader("7", "Přídání měsíce k zadanému datu", False)
DAYSINMONTH = calendar.monthrange(TODAY.year, TODAY.month)[1]
print(TODAY + timedelta(days=DAYSINMONTH))

# 8. Vypsání řádku hodnot po určitém čase
# Požadované: namespace time viz. line 4
Classes.UserInterface.PrintHeader("8", "Vypsání řádku hodnot po určitém čase", False)
x = 0
while x < 5:
    time.sleep(1)
    print("Slept for 1 sec.")
    x = x + 1
    
# 9. Výpis datumů se zadaným intervalem
Classes.UserInterface.PrintHeader("9", "Vypsání řádku hodnot po určitém čase", False)
def Every3Days(date):
    print("Start date: {insertedDay}".format(insertedDay=date))
    print("Next 3 days: ")
    for _ in range(3):
        date = date + datetime.timedelta(days=3)
        print("{d}".format(d=date))

Every3Days(datetime.date(2018, 2, 1))

# 10. Zobrazení daného měsíce
cal = calendar.TextCalendar(calendar.MONDAY)
print("First month - 2018")
print(cal.prmonth(2018, 1))