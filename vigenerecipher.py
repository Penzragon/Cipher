alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol = "~`!@#$%^&*()_-+=;:'\",.? "


def vigenere(message, keyword):
    pointer = 0
    keyworded = ""
    decoded = ""
    for i in range(len(message)):
        if not message[i] in symbol:
            keyworded += keyword[pointer]
            pointer = (pointer + 1) % len(keyword)
        else:
            keyworded += message[i]
    for i in range(len(message)):
        if not message[i] in symbol:
            lenght = alphabet.find(message[i]) - alphabet.find(keyworded[i])
            decoded += alphabet[lenght % 26]
        else:
            decoded += message[i]
    return decoded


def vigenere_coder(message, keyword):
    pointer = 0
    keyworded = ""
    coded = ""
    for i in range(len(message)):
        if not message[i] in symbol:
            keyworded += keyword[pointer]
            pointer = (pointer + 1) % len(keyword)
        else:
            keyworded += message[i]
    for i in range(len(message)):
        if not message[i] in symbol:
            length = alphabet.find(message[i]) + alphabet.find(keyworded[i])
            coded += alphabet[length % 26]
        else:
            coded += message[i]
    return coded


message = "rifky aliffa"
keyword = "penzragon"

print(vigenere(vigenere_coder(message, keyword), keyword))
print(vigenere_coder(message, keyword))
