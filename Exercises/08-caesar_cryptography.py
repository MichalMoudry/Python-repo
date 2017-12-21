def caesar_encrypt(text, step):
    outText = []
    cryptText = []

    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J"]
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "ch", "i", "j"]

    for letter in text:
        if letter in uppercase:
            index = uppercase.index(letter)
            crypting = (index + step) % 11
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif letter in lowercase:
            index = lowercase.index(letter)
            crypting = (index + step) % 11
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText

code = caesar_encrypt("abcd", len("abcd"))
print("\n", code, "\n")
