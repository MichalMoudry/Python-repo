platidla = [1, 2, 2, 5]
while platidla[-1] < 5000:
    platidla.append(platidla[-3] * 10)
platidla.reverse()

castka = input("Zadejte částku: ")
temp = castka.isdigit()
if temp:
    castka = int(castka)
    for bankovka in platidla:
        if castka // bankovka == 0:
            continue
        else:
            print(castka // bankovka, "x", bankovka)
            castka = castka % bankovka
else:
    print("Error")
input("Press any key to exit...")