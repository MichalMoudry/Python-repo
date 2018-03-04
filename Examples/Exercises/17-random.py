import random
from Classes import Classes

LIST = [1, 2, 11, 3, 4, 6, 12, 30]

Classes.UserInterface.PrintHeader("1", "Náhodné číslo", True)
print(random.randint(1, 30))

Classes.UserInterface.PrintHeader("2", "Náhodné pole ze seznamu", False)
print("Seznam: ", LIST)
print("Vybrané pole: ", random.choice(LIST))

Classes.UserInterface.PrintHeader("3", "Zamíchání seznamu", False)
print("Původní seznam: ", LIST)
random.shuffle(LIST)
print("Seznam po zamýchání: ", LIST)

Classes.UserInterface.PrintHeader("4", "Vybrání náhodných hodnot", False)
print(random.sample(LIST, 3))