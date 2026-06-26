name = input("Name des Kunden: ")
anfrage = input("Anfrage des Kunden: ")
telefon = input("Telefonnummer:")

kunde = {
    "name": name,
    "anfrage": anfrage,
    "telefon": telefon
}

print()
print("Kundendaten gespeichert:")
print("Name:", kunde["name"])
print("Anfrage:", kunde["anfrage"])