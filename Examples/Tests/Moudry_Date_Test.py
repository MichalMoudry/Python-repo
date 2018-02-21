import datetime
import time

NOW = datetime.datetime.now()
print("Now: ", NOW)
print("Year: ", NOW.year)
print("Month: ", NOW.strftime("%B"))
print("Week number: ", NOW.strftime("%V"))
print("Day number in week: ", NOW.weekday())
print("Day number in month: ", NOW.strftime("%d"))
print("Day number in year: ", NOW.strftime("%j"))
print("Day name: ", NOW.strftime("%A"))

input("Press any key to exit...\n")