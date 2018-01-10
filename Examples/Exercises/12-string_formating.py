import math

SENTENCE = "Test sentence"
print("s =>", SENTENCE.find("s"))
print("Test %s" % "sentence")
print("Test: %s" % SENTENCE)

"""
Formátování metodou
"""
print("From {date}".format(date="morning"))
print("{:<25}".format("Align left"))
print("{:>25}".format("Align right"))

"""
Math module
"""
print("Pi number: {0:.50f}".format(math.pi))

input("Press any key to exit...")