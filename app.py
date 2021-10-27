# siege = int(input("siege: "))//5
# unentschieden = int(input("unentschieden: "))//4
# niederlagen = int(input("niederlagen: "))//3

# def berechnePunkte(s, u, n):
#     punktzahl = s*3 + u*1 + n*0
#     return punktzahl

# p = berechnePunkte(siege, unentschieden, niederlagen)
# print("Die Fußballmannschaft hat folgende Punktzahl erreicht: ",p)

# siege = int(input("siege: "))//5
# unentschieden = int(input("unentschieden: "))//4
# niederlagen = int(input("niederlagen: "))//3

# def berechnePunkte(s, u, n):
#     punktzahl = s*3 + u*1 + n*0
#     return punktzahl

# p = berechnePunkte(siege, unentschieden, niederlagen)
# print("Die Fußballmannschaft hat folgende Punktzahl erreicht: ",p)

# EINGABE

# grundseite = float(input("Grundseite eingeben: "))
# hoehe = float(input("Höhe eingeben: "))


# # VERARBEITUNG

# def flaecheDreieck(g, h):
#     return g * h / 2

# try:
# # AUSGABE
#     print("Flächeninhalt:", flaecheDreieck(grundseite, hoehe))

# except:
#     print("Bitte eine Zahl eingeben!")

# """
# Problem: Wie im Unterricht besprochen, ist es nicht ganz so intuitiv ein "Entweder-Oder" in Python abzubilden.

# Aufgabe: Entwickle eine "Entweder-Oder"-Funktion. Diese Funktion sollte 2 Parameter erhalten und entweder True oder False zurückgeben.
		 
# 		 Regel 1: True wird zurückgegeben, wenn einer der beiden Parameter True ist aber der andere False.
# 		 Regel 2: False wird zurückgegeben, wenn Regel 1 nicht erfüllt.

# 		 Testen kannst du die Funktion mit folgenden Parametern (Vorausgesetzt du hast sie xor genannt): 
		 
# 		 print(xor(True, False)) # sollte True zurückgeben
# 		 print(xor(True, True)) # sollte False zurückgeben
# 		 print(xor(False, True)) # sollte True zurückgeben
# 		 print(xor(False, False)) # sollte False zurückgeben
# 		 print(xor(5 > 3, 10 < 1)) # sollte True zurückgeben
# 		 print(xor("5" != 5, 5 != 5)) # sollte True zurückgeben
		 
# 		 Sowas geht auch, wird aber in der BONUS-Aufgabe "gefixt":
# 		 print(xor(1, 0)) # sollte True zurückgeben
# 		 print(xor("abc", "def")) # sollte False


# BONUS: Die Funktion sollte als Parameter nur boolsche Werte erlauben (dazu gehören auch Ausdrücke, die einen boolschen Wert ausgeben!)
# 	   Ergänze deine Funktion mit diesem Feature.
# 	   Tipp: Nutze die type()-Funktion! Aber welche Ausgabe würdest du von der Funktion erwarten?	 
# Problem: Wie im Unterricht besprochen, ist es nicht ganz so intuitiv ein "Entweder-Oder" in Python abzubilden.

# Aufgabe: Entwickle eine "Entweder-Oder"-Funktion. Diese Funktion sollte 2 Parameter erhalten und entweder True oder False zurückgeben.
		 
# 		 Regel 1: True wird zurückgegeben, wenn einer der beiden Parameter True ist aber der andere False.
# 		 Regel 2: False wird zurückgegeben, wenn Regel 1 nicht erfüllt.

# 		 Testen kannst du die Funktion mit folgenden Parametern (Vorausgesetzt du hast sie xor genannt): 
		 
# 		 print(xor(True, False)) # sollte True zurückgeben
# 		 print(xor(True, True)) # sollte False zurückgeben
# 		 print(xor(False, True)) # sollte True zurückgeben
# 		 print(xor(False, False)) # sollte False zurückgeben
# 		 print(xor(5 > 3, 10 < 1)) # sollte True zurückgeben
# 		 print(xor("5" != 5, 5 != 5)) # sollte True zurückgeben
		 
# 		 Sowas geht auch, wird aber in der BONUS-Aufgabe "gefixt":
# 		 print(xor(1, 0)) # sollte True zurückgeben
# 		 print(xor("abc", "def")) # sollte False


# BONUS: Die Funktion sollte als Parameter nur boolsche Werte erlauben (dazu gehören auch Ausdrücke, die einen boolschen Wert ausgeben!)
# # 	   Ergänze deine Funktion mit diesem Feature.
# # 	   Tipp: Nutze die type()-Funktion! Aber welche Ausgabe würdest du von der Funktion erwarten?	 
# # """
# def xor(a, b):
#     if a != b:
#         return True
#     else:
#         return False


# print(xor(True, False)) # sollte True zurückgeben
# print(xor(True, True)) # sollte False zurückgeben
# print(xor(False, True)) # sollte True zurückgeben
# print(xor(False, False)) # sollte False zurückgeben
# print(xor(5 > 3, 10 < 1)) # sollte True zurückgeben
# print(xor("5" != 5, 5 != 5)) # sollte True zurückgeben


# print(xor(1, 0)) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben
# print(xor("abc", "def")) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben
# print(xor(True, 1)) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben

# # print(xor(True, False)) # sollte True zurückgeben
# # print(xor(True, True)) # sollte False zurückgeben
# # print(xor(False, True)) # sollte True zurückgeben
# # print(xor(False, False)) # sollte False zurückgeben
# # print(xor(5 > 3, 10 < 1)) # sollte True zurückgeben
# # print(xor("5" != 5, 5 != 5)) # sollte True zurückgeben


# # print(xor(1, 0)) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben
# # print(xor("abc", "def")) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben
# # print(xor(True, 1)) # sollte "Datentyp von mind. einem Parameter passt nicht!" zurückgeben

# for i in range(3):
#     user_input = int(input("gebe bitte deine Zahlen ein, die nur duch 2 teilbar ist:"))
#     if user_input % 2 !=0:
#         print("Eingabe ungültig")
#         continue
#     else:
#         print(user_input)




