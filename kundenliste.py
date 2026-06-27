kunden = [
    {
        "name": "Felix",
        "anfrage": "Neue Garage",
        "telefon": "0123456789"
    },
    {
        "name": "Max",
        "anfrage": "Neue Terrasse",
        "telefon": "0234567890"
    },
    {
        "name": "Anna",
        "anfrage": "Neues Dach",
        "telefon": "0345678901"
    },
    {
        "name": "Tim",
        "anfrage": "Neue Einfahrt",
        "telefon": "0456789012"
    }
]

for kunde in kunden:
    print("Name:", kunde["name"])
    print("Anfrage:", kunde["anfrage"])
    print("telefon:", kunde["telefon"])
    print("----------------")