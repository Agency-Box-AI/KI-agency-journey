while True:

    print()
    print("1 = Kunde hinzufügen")
    print("2 = Kunden anzeigen")
    print("3 = Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":

        name = input("Name: ")
        anfrage = input("Anfrage: ")

        with open("kunden.txt", "a") as datei:
            datei.write(name + " - " + anfrage + "\n")

    elif auswahl == "2":

        with open("kunden.txt", "r") as datei:
            print(datei.read())

    elif auswahl == "3":
        break