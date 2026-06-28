with open("kunden.txt", "r") as datei:
    kunden = datei.readlines()

print("Anzahl Kunden:", len(kunden))