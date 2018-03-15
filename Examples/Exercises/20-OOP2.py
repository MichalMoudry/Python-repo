from Classes import UserInterface

class Person:
    def __init__(self, name = "", age = 0):
        self.__name = name
        self.__age = age

    #Ekvivalenta override .ToString() v C#
    def __str__(self):
        return str(self.__name)

    def __repr__(self):
        return str("Osoba ({0})".format(self))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, inputAge):
        self.__age = inputAge

UserInterface.UserInterface.PrintHeader("1", "Osoby", True)
PERSON1 = Person("Michal Moudrý", 19)
PERSON2 = Person("Test user 1", 19)
print("Osoba 1: {0} (id: {1})\nOsoba 2: {2} (id: {3})".format(PERSON1, id(PERSON1), PERSON2, id(PERSON2)))

UserInterface.UserInterface.PrintHeader("2", "Přiřazení", False)
print("{0} => {1}".format(PERSON1, PERSON2))
PERSON1 = PERSON2
print("Osoba 1: {0} (id: {1})\nOsoba 2: {2} (id: {3})".format(PERSON1, id(PERSON1), PERSON2, id(PERSON2)))

UserInterface.UserInterface.PrintHeader("3", "Kopírování", False)
PERSON1 = Person("Michal Moudrý", 19)
PERSON3 = eval(repr(PERSON1))
print("Osoba 1: {0} (id: {1})\nOsoba 2: {2} (id: {3})\nOsoba 2: {4} (id: {5})".format(PERSON1, id(PERSON1), PERSON2, id(PERSON2), PERSON3, id(PERSON3)))