name = input("Name des Kunden: ")
anfrage = input("Anfrage des Kunden: ")

with open("kunden.txt", "a") as datei:
    datei.write(name + " - " + anfrage + "\n")

print("Kunde gespeichert!")