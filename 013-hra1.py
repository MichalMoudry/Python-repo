from random import randint
moznosti = ["kamen", "nuzky", "papir"]
isReturn = True
returnNum = 1

while isReturn:
    returnNum = returnNum + 1
    tahPocitace = moznosti[randint(0, 2)]
    tahHrace = input("1 - kamen\n2- nuzky\n3 - papir\nVstup: ")
    
    if tahHrace == "1":
        print("Vas vstup: ", "kamen", "|", "Vstup pocitace: ", tahPocitace)
        if tahPocitace == "kamen":
            print("Vysledek: remiza")
        elif tahPocitace == "nuzky":
            print("Vysledek: vyhra")
        elif tahPocitace == "papir":
            print("Vysledek: prohra")
        
    elif tahHrace == "2":
        print("Vas vstup: ", "nuzky", "|", "Vstup pocitace: ", tahPocitace)
        if tahPocitace == "kamen":
            print("Vysledek: prohra")
        elif tahPocitace == "nuzky":
            print("Vysledek: remiza")
        elif tahPocitace == "papir":
            print("Vysledek: vyhra")
        
    elif tahHrace == "3":
        print("Vas vstup: ", "papir", "|", "Vstup pocitace: ", tahPocitace)
        if tahPocitace == "kamen":
            print("Vysledek: vyhra")
        elif tahPocitace == "nuzky":
            print("Vysledek: prohra")
        elif tahPocitace == "papir":
            print("Vysledek: remiza")
        
    else:
        print("Wrong input...")

    userDecision = input("Chcete dalsi kolo?[Y/N]: ")
    if userDecision == "N":
        print("Pocet odehranych kol: ", returnNum - 1)
        isReturn = False
    else:
        print("")
        print("-----------Kolo c.", returnNum,"-----------")
        print("")

print("")
input("Stisknete klavesu pro ukonceni...")
