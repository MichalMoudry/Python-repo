isReturn = True
while isReturn:
    print("Vyberte program:", "\n1 - Výpočet objemu kvádru", "\n2 - Výpis * znaků", "\n3 - Kalkulačka", "\n4 - Tabulka násobilky")
    program = input("Čislo programu: ")
    if program == "1":
            length = input("Délka kvádru: ")
            width = input("Šířka kvádru: ")
            height = input("Výška kvádru: ")
            if (length != "") &  (width != "") & (height != ""):
                length = int(length)
                width = int(width)
                height = int(height)
                print(length * width * height)

    if program == "2":
        num = input("Počet znaků *: ")
        if num != "":
            num = int(num)
            char = ""
            for i in range(0, num):
                char += "*"
                print(char)
            for x in range(0, (num - 1)):
                char = char[: -1]
                print(char)

    if program == "3":
        num1 = input("Číslo 1: ")
        num2 = input("Číslo 2: ")
        operace = str(input("Operace [ + | - | * | : ]: "))
        if operace != "":
            num1 = int(num1)
            num2 = int(num2)
            if operace == "+":
                print(num1, "+", num2, "=", num1 + num2)
            elif operace == "-":
                print(num1, "-", num2, "=", num1 - num2)
            elif operace == "*":
                print(num1, "*", num2, "=", num1 * num2)
            elif (operace == ":") & num2 > 0:
                print(num1, ":", num2, "=", num1 / num2)

    if program == "4":
        number = input("Zadejte číslo: ")
        if number != "":
            number = int(number)
            for i in range(1, 11):
                print(number, "*", i, "=", number * i)
            
    
    decision = str(input ("Chcete pokračovat [Y/N]? "))
    if decision == "N":
        isReturn = False
    elif decision != "N":
        print("")
        print("--------")
        print("")
