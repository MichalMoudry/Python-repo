print("----Character appending----")
print("")
text_1 = "Test text"
letter_2 = "|"

for letter in text_1:
    print(letter + letter_2)

print("----Cycle break----")
print("Original word: Python")
for letter in "Python":
    if letter is "h":
        break
    print("Letter: ", letter)

print("")
print("----Cycle continue----")
tempInt = 6
print("Init number: ", tempInt)
while tempInt > 2:
    tempInt = tempInt - 1
    if tempInt == 3:
        continue
print("Number after cycle: ", tempInt)

print("")
print("----ASCII table number----")
print("a", "=>", ord("a"))
print("b", "=>", ord("b"))
print("c", "=>", ord("c"))

print("")
input("Press any key to exit...")