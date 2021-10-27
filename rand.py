"""
Erstelle ein Programm, welches eine zufällige
Zahl generiert (zwischen 0 und 10) und den
User bittet diese Zahl zu erraten.

Um eine zufällige Zahl zu generieren, kannst du folgendermaßen vorgehen:

import random
rand_nr = random.randint(0, 10)

BONUS 1: Weise den User darauf hin, dass seine Zahl außerhalb des gültigen
         Wertebereichs liegt.

BONUS 2: Der User soll eine begrenzte Anzahl Versuche haben (z.B. 3).
         Sollte er es innerhalb dieser Versuche nicht schaffen die Zahl
         zu erraten, gilt das Spiel als verloren.

BONUS 3: Gib dem User Tipps, dass seine Zahl höher oder niedriger als die
         gesuchte Zahl ist.

"""
from random import randint
# print(rand_nr)
versuche = 3
rand_nr = randint(0, 10)

while versuche != 0:
    user = int(input(f"Bitte geben Sie eine Zahl zwischen 0 und 10 ein. Sie haben {versuche} Versuche: "))
    if user > rand_nr:
        print("Ihre Zahl ist größer als die vom Computer")
        print(user)
    elif user < rand_nr:
        print("Ihre Zahl ist kleiner als die vom Computer")
        print(user)
    versuche = versuche -1
    if rand_nr == user:
        print("Glückwunsch!")
        print("Möchten Sie weiterspielen(y) oder aufhören(n)?")
        eingabe = input()
        if eingabe == "y":
            versuche = 3
            rand_nr = randint(0, 10)
            continue
        elif eingabe == "n":
            print("Tschüss!")
            break
    if user > 10 or user < 0:
        print("Ungültige Eingabe. Die Zahl muss zwischen 0 und 10 liegen!")
        continue
    
    if versuche == 0:
        print(f"Sie haben leider verloren. Die gesuchte Zahl war:  {rand_nr}")
        print("Möchten Sie weiterspielen(y) oder aufhören(n)?")
        eingabe = input()
        if eingabe == "y":
            versuche = 3
            rand_nr = randint(0, 10)
            continue
        elif eingabe == "n":
            print("Tschüss!")
            break
