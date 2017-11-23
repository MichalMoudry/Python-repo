for i in range(1, 35):
    if ((i%3 == 0) | (i%7 == 0)) == True & ((i%3 == 0) & (i%7 == 0) == False):
        print(i)
