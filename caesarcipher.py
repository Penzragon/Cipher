alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol = "~`!@#$%^&*()_-+=;:'\",.? "


def decoder(message, offset):
    decoded = ""
    for letter in message:
        if not letter in symbol:
            value = alphabet.find(letter)
            decoded += alphabet[(value - offset) % 26]
        else:
            decoded += letter
    return decoded


def coder(message, offset):
    coded = ""
    for letter in message:
        if not letter in symbol:
            value = alphabet.find(letter)
            coded += alphabet[(value + offset) % 26]
        else:
            coded += letter
    return coded


while True:
    start = 0
    end = 50
    print(
        """
        =====================
        1. Decode a message
        2. Code a message
        3. Exit
        =====================
        """
    )
    menu = input("Pilih menu: ")
    if menu == "1":
        print("""
        =====================
            DECODE MESSAGE
        =====================
        """)
        message = input("Masukan pesan: ")
        print("""
        Apa anda tau offsetnya?
        1. Ya
        2. Tidak
        """)
        pilihan = input("Masukan pilihan: ")
        if pilihan == "1":
            ofset = input("Masukan offset: ")
            print("DECODED MESSAGE: {}".format(decoder(message, int(ofset))))
        elif pilihan == "2":
            while True:
                for i in range(start, end):
                    print(i, decoder(message, i))
                print("""
                Is the message decoded?
                1. Ya
                2. Tidak
                """)
                apakah = input("pilihan: ")
                if apakah == "1":
                    break
                elif apakah == "2":
                    start = end
                    end += 50
    elif menu == "2":
        print("""
        =====================
            CODE MESSAGE
        =====================
        """)
        message = input("Masukan pesan: ")
        ofset = input("Masukan offset: ")
        print("CODED MESSAGE: {}".format(coder(message, int(ofset))))
    elif menu == "3":
        print("EXITING PROGRAM. . .")
        break
