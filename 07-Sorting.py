cisla = input("Zadejte čísla: ")
cisla = cisla.split()

zaporna = []
nezaporna = []

for i in cisla:
    i = int(i)
    if i >= 0:
        nezaporna.append(i)
    else:
        zaporna.append(i)

final = zaporna + nezaporna
print(final)
