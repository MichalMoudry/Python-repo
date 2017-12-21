def PrintTitle(RequestedTitle):
    print("----", RequestedTitle, "----")

str = "alpha"
lst = ["pi", 3.14, 8]
tup = ("g", 3.72, 8)
set = {"e", 3.3, 8}
dct = {"pi" : 3.14, "g" : 2.72, "e" : 3.3}
numbers = list(range(10))

PrintTitle("Normal")
for x in numbers:
    print(x)

PrintTitle("In line")
for x in numbers:
    print(x, end=" ")

PrintTitle("%3")
for y in numbers:
    if y%3 == 0:
        print(y)

print(PrintTitle("**2"))
print(numbers)
print("=>")
for index in range(len(numbers)):
    numbers[index] = numbers[index]**2
print(numbers)

PrintTitle("Enumerate")
numbers = list(range(10))
for index, value in enumerate(numbers):
    print("(", index, "=>", value, ")")

PrintTitle("End")
input("Press any key to exit...")