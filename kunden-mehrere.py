while True:
    name = input("Name: ")
    anfrage = input("Anfrage: ")

    with open("kunden.txt", "a") as datei:
        datei.write(name + " - " + anfrage + "\n")

    weiter = input("Weiteren Kunden eingeben? (ja/nein): ")

    if weiter == "nein":
        break