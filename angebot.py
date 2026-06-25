kunde = input("Name des Kunden: ")
anfrage = input("Worum geht es? ")

if "Terrasse" in anfrage:
    hinweis = "Wir haben bereits viele Terrassen erfolgreich gebaut."

elif "Dach" in anfrage:
    hinweis = "Unsere Dach-Experten werden Ihre Anfrage prüfen."

elif "Garage" in anfrage:
    hinweis = "Wir erstellen gerne ein individuelles Garagen-Angebot."

elif "Auffahrt" in anfrage:
    hinweis = "Wir bauen gerne für sie eine Individuelle auffahrt, haben sie eine Preisvorstellung?"

else:
    hinweis = "Vielen Dank für Ihre Anfrage."

antwort = f"""
Sehr geehrte/r {kunde},

vielen Dank für Ihre Anfrage.

Anfrage:
{anfrage}

{hinweis}

Wir melden uns schnellstmöglich.

Mit freundlichen Grüßen
Ihr Handwerksbetrieb
"""

print(antwort)