cisla = list(range(50))
for num in cisla:
    index = cisla.index(num)
    temp1 = index - 1
    temp2 = index - 2
    num1 = cisla[temp1]
    num2 = cisla[temp2]
    print(num)
    print("Count: ", cisla[index], "(", num1, "+", num2,")")
    temp = num1 + num2
    print("Res: ", temp, "\n--------------")
