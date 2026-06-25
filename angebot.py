kunde = input("Name des Kunden: ")
anfrage = input("Worum geht es? ")

antwort = f"""
Sehr geehrte/r {kunde},

vielen Dank für Ihre Anfrage.

Bezüglich Ihrer Anfrage:

"{anfrage}"

werden wir uns schnellstmöglich bei Ihnen melden und Ihnen ein individuelles Angebot erstellen.

Mit freundlichen Grüßen

Ihr Handwerksbetrieb
"""

print(antwort)