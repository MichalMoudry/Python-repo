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
while isReturn:
    print("Kostka hozena")
    print("Výsledek hodu: {res}".format(res=DICE.Roll()))
    decision = str(input ("Chcete pokračovat [Y/N]? "))
    if decision == "N":
        isReturn = False
    else:
        isReturn = True
        print("")
        print("--------")
        print("")