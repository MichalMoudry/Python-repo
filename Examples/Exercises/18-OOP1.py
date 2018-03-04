from Classes import UserInterface

class Test:
    def __init__(self, text = ""):
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    def pozdrav(self, JMENO):
        print("Vložené jméno: {name}".format(name=JMENO))
        if self.__text != "":
            print("Vložený text: {text}".format(text=self.__text))

UserInterface.UserInterface.PrintHeader("1", "", True)
TEST = Test()
TEST.text = "Moudrý"
TEST.pozdrav("Michal")