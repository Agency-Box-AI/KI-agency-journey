name = input("Name: ")
anfrage = input("Anfrage: ")
telefon = input("Telefon: ")

with open("kunden.txt", "a") as datei:
    datei.write(name + " | " + anfrage + " | " + telefon + "\n")

print("Kunde gespeichert!")