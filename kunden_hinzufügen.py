kunden = []

for i in range(3):
    print()
    print("Kunde", i + 1)

    name = input("Name: ")
    anfrage = input("Anfrage: ")
    telefon = input("Telefon: ")

    kunde = {
        "name": name,
        "anfrage": anfrage,
        "telefon": telefon
    }

    kunden.append(kunde)

print()
print("Gespeicherte Kunden:")
print("--------------------")

for kunde in kunden:
    print("Name:", kunde["name"])
    print("Anfrage:", kunde["anfrage"])
    print("telefon:", kunde["telefon"])
    print("--------------------")