def LargestNumInList(listParam):
    num = 0
    for i in listParam:
        fieldCheck = isinstance(i, int)
        if fieldCheck == True:
            if i > num:
                num = i
    return num

targetedList = list([2, 13, 3, "f", 5, 4, 12])
print("Inserted list: ", targetedList)
print("Largest number in list: ", LargestNumInList(targetedList))
input("Press any key to exit...")