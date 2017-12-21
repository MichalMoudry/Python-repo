isReturn = True
pokusy = 0
while isReturn:
    userInput = input ("Napište číslo větší než 100: ")
    if userInput != "":
        userInput = int(userInput)
        pokusy = pokusy + 1
        print("Počet pokusů: ", pokusy)
        if userInput >= 100:
            print("Zadali jste větší číslo než 100")
            pokusy = 0
            isReturn = False
        decision = str(input ("Chcete pokračovat [Y/N]? "))
        if decision == "N":
            isReturn = False
        elif decision == "Y":
            isReturn = True
            print("")
            print("--------")
            print("")
    else:
        print("Error")
