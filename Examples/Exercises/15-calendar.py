import datetime
from datetime import date, timedelta
import calendar
import time
from Classes import Classes

# 1. Kalendář se zadaným rokem a měsícem
Classes.UserInterface.PrintHeader("1", "Kalendář se zadaným rokem a měsícem", True)
MONTH = str(input("Zadejte měsíc: "))
YEAR = str(input("Zadejte rok: "))
MONTHCHECK = MONTH.isdigit()
YEARCHECK = YEAR.isdigit()

if MONTHCHECK and YEARCHECK:
    MONTH = int(MONTH)
    YEAR = int(YEAR)
    if MONTH < 13:
        calendar.setfirstweekday(calendar.MONDAY)
        CALENDAR = calendar.monthcalendar(YEAR, MONTH)

        if len(str(MONTH)) is 1:
            MONTH = "0%s" % MONTH

        # Záhlaví kalendáře
        print("|****** %s-%s *******|" % (MONTH, YEAR))
        print("|Po Út St Čt Pá So Ne|")
        print("|--------------------|")

        # Zobrazení kalendáře
        BORDER = "|"
        for WEEK in CALENDAR:
            LINE = BORDER
            for DAY in WEEK:
                if DAY is 0:
                    LINE += "   "
                elif len(str(DAY)) is 1:
                    LINE += " %d " % DAY
                else:
                    LINE += "%d " % DAY
            LINE = LINE [0:len(LINE) - 1]
            LINE += BORDER
            print(LINE)
        print("|--------------------|")
    else:
        print("Wrong month...")
else:
    print("Error occured...")

input("Press any key to exit...")