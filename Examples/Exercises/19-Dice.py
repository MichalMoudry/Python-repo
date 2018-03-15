from Classes import UserInterface
import random

class Dice():
    def __init__(self, result = 0, sides = 6):
        self.__result = result
        self.__sides = sides

    @property
    def result(self):
        return self.__result

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, sides):
        self.__sides = sides

    def Roll(self):
        self.__result = random.randint(1, self.__sides)
        return self.result

UserInterface.UserInterface.PrintHeader("1", "Hrací kostka", True)
isReturn = True
DICE = Dice()
RESULT = 0
while isReturn:
    SIDES = 6
    try:
        SIDES = int(input("Počet stran kostky: "))
    except ValueError:
        print("Špatný vstup => počet stran kostky je 6\n")
    DICE.sides = SIDES
    ROLLRESULT = DICE.Roll()
    RESULT = RESULT + ROLLRESULT
    print("Výsledek hodu: {res}".format(res=ROLLRESULT))
    decision = str(input ("Chcete pokračovat [Y/N]? "))
    if decision == "N":
        isReturn = False
        UserInterface.UserInterface.PrintHeader("", "Výsledek všech hodů", False)
        print(RESULT, "\n")
    else:
        isReturn = True
        print("")
        UserInterface.UserInterface.PrintHeader("", "Nový hod", False)
        print("")