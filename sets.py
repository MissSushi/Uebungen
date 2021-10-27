"""
Aufgabe 1) Erstelle eine Menge mit deinen Lieblingsfarben (oder beliebigen Farben).
"""
color = {"blau", "rot"}


"""
Aufgabe 2) Erstelle eine Liste mit den Werten "Schwarz" und "Weiß".
"""
list = ["schwarz", "weiß"]


"""
Aufgabe 3) Füge der Menge aus Aufgabe 1) den Wert "Neongrün" hinzu.
"""
color.add("neongrün")



"""
Aufgabe 4) Füge der Menge aus Aufgabe 1) (inkl. Veränderungen aus Aufgabe 3)
		   die Elemente der Liste aus Aufgabe 2 hinzu.
"""
color.update(list)




"""
Aufgabe 5) Entferne den Wert "Weiß" aus der Menge.
"""
color.discard("weiß")

"""
Aufgabe 6) Ermittle die Anzahl der Elemente der Menge.
"""
#print(len(color))




"""
Aufgabe 7) Entwickle eine Funktion, welche die einzigartigen Buchstaben
		   eines Wortes zählt und den Wert als Integer zurückgibt.

Anmerkung: Groß- und Kleinbuchstaben sind unterschiedliche Buchstaben.

Beispiele:
"Python" 	-> 6
"Pythonnn"	-> 6
"pPython"	-> 7
"""
def counter(wort):
    return(len(set(wort)))
print(counter("Python"))




"""
BONUS) Entwickle eine Funktion, welche die Vokale eines Wortes entfernt.

Vokale sind die Buchstaben a e i o u

Die Funktion erhält als Parameter:
	- Eine Zeichenkette

Die Funktion gibt zurück:
	- Eine Zeichenkette (ohne Vokale)

Beispiel:
"abecidoefuuu"
wird zu
"fdcb"	# bzw. "{'f', 'd', 'c', 'b'}" wenn du Sets nutzt

Anmerkung: Wenn du Sets zu Strings formatierst, bleibt die Syntax
des Sets bestehen. Mache dir zunächst keine Gedanken darüber, das 
wird in der nächsten Aufgabe gefixt :)  
 
Anmerkung 2: Die Buchstaben, die zurückgegeben werden, müssen nicht
die gleiche Reihenfolge haben, die das Wort ursprünglich hatte.
"""





"""
ULTRABONUS) Verbessere deine Funktion aus der BONUS)-Aufgabe:

- Die Funktion sollte nicht mehr die String-Darstellung von Mengen zurückgeben.

- Erweitere die Funktion um einen weiteren Parameter, welcher alle Buchstaben
beinhaltet, die entfernt werden sollen. Damit sollen nicht nur Vokale sondern
alle Buchstaben aus dem 2. Parameter entfernt werden können.
"""