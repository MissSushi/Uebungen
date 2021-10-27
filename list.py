"""
Aufgabe 1) Erstelle eine Liste mit folgenden Elementen:
		   
		   - Eine Zeichenkette mit den ersten beiden Buchstaben deines Vornamens (oder 2 zufällige Buchstaben)
		   - Eine Zeichenkette mit den letzten drei Buchstaben deines Nachnamens (oder 3 zufällige Buchstaben)
		   - Dem booleschen Wahrheitswert für Wahr
		   - Deine Lieblingszahl (oder eine zufällige Zahl)
		   - Dem booleschen Wahrheitswert für Falsch
"""

liste = ["Me","Six", True, 13, False]

"""
Aufgabe 2) Erstelle eine weitere Liste mit folgenden Elementen:
		   
		   - Der Ganzzahl Zwei
		   - Dem Ergebnis von 1/2
		   - Der Zeichenkette abc
"""

liste2 = [2, 1/2, "abc"]

"""
Aufgabe 3) Führe für die in Aufgabe 1 erstellte Liste folgende Befehle aus:
"""	
# a) Gebe das erste Element aus.
print(liste[0])
# b) Gebe das vorletzte Element aus.
print(liste[-2])
# c) Gebe alle Elemente aus, außer dem Ersten und dem Letzten.
print(liste[1:-1])
# d) Entferne den letzten Wert.
liste.pop()
# e) Multipliziere deine Lieblingszahl mit 12 (inkl. Verändern der Liste).
print(liste[3]*12)
# f) Füge die Ganzzahl 100 ganz vorne ein (Index 0).
liste.insert(0, 100)
# g) Erweitere die Liste um die Elemente der in Aufgabe 2 erstellten Liste.
liste.extend(liste2)

print(liste)
"""
BONUS) Führe für die in Aufgabe 1 erstellte und in 3) ordentlich veränderte :) Liste folgende Befehle aus:
"""

# a) Gebe die Häufigkeit des boolschen Wahrheitswert True aus.
print(liste.count(True))

# b) Gebe die Länge der Liste aus.
print(len(liste))

# c) Entferne den boolschen Wahrheitswert True.
# 	 (Schreibe den Befehl so, dass er keinen Fehler anzeigt, wenn das Element nicht existiert!)
if True in liste:
	liste.remove(True)
if True in liste:
	liste.remove(True)
print(liste)

"""
ULTRABONUS) Schreibe eine Funktion safe_remove() mit der Listenelemente sicher entfernt werden können.
		    - Die Funktion sollte nur dann versuchen etwas zu entfernen, wenn es in der Liste ist.
			- Überlege dir, welche 2 Parameter benötigt werden
			- Die Funktion gibt die (evtl. veränderte) Liste aus
			- Teste deine Funktion indem du sie aufrufst
"""
def safe_remove(liste, elemente):
	for i in elemente:
		if i in liste:
			liste.remove(i)
	return liste
print(safe_remove(liste, ["Butter", "Me"]))
"""if elem in liste:
liste.remove(elemente)
return list"""