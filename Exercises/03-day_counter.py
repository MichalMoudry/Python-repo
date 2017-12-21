def GetDay(num):
    num = num%7
    return num

isReturn = True
while isReturn:
    today = int (input ("Číslo dne: "))
    days = int (input ("Počet dní pryč: "))
    print(GetDay(today + days))
    decision = str(input ("Chcete pokračovat [Y/N]? "))
    if decision == "N":
        isReturn = False
    elif decision == "Y":
        print("")
        print("--------")
        print("")