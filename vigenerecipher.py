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


while True:
    print(
        """
        1. Decode A Message
        2. Code A Message
        3. Exit
        """
    )
    menu = input(": ")
    try:
        menu.strip()
        menu = int(menu)
    except:
        menu = input(": ")
    if menu == 1:
        message = input("Input your message: ")
        keyword = input("input your keyword: ")
        print(
            f"Decoded message: {vigenere(message.lower(), keyword.lower())}")
    elif menu == 2:
        message = input("Input your message: ")
        keyword = input("input your keyword: ")
        print(
            f"Coded message: {vigenere_coder(message.lower(), keyword.lower())}")
    elif menu == 3:
        print("Exiting Program. . .")
        break
    else:
        print("Wrong Input!")
