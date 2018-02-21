import datetime
from datetime import datetime
from datetime import date, timedelta

NOW = datetime.now()

# 1. Strptime metoda
DATE = datetime.strptime("Jan 1 2018", "%b %d %Y")
print(DATE)

# 2. Dnešní datum a čas
print("Dnešní datum a čas: ", NOW)

# 3. Odčítání dnů
SUBTRACTED_DATE = NOW - timedelta(5)
print("Dnešní datum a čas: ", NOW)
print("Před 5 dny: ", SUBTRACTED_DATE)

input("Press any key to exit...")