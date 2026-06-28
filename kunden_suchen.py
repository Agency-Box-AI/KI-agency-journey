suchbegriff = input("Name suchen: ")

with open("kunden.txt", "r") as datei:
    for zeile in datei:
        if suchbegriff in zeile:
            print(zeile)