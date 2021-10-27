"""Spielregeln Schere, Stein, Papier:
Schere gewinnt gegen Papier
Stein gewinnt gegen Schere
Papier gewinnt gegen Stein

Alle Fälle:

p1 gewinnt wenn:
p1 schere und computer papier
p1 papier und computer stein
p1 stein und computer Schere

p1 verliert wenn:
p1 schere und computer Stein
p1 Stein und computer papier
p1 papier und computer schere

Unentschieden wenn:
p1 schere und compjuter schere
p1 papier und computer papier
p1 stein und computer stein

"""
#Randint wird aus random importiert. Randint gibt die im Parameter genannten Zufallszahlen aus.
from random import randint
computer = randint(1,3)

#User Eingabe
p1 = str(input("Bitte geben Sie 's' für Schere, 'r' für Stein und 'p' für Papier ein: "))

#Die Zufallszahlen werden in Wörter umgewandelt. 1 für Schere, 2 für Stein und 3 für Papier
if computer == 1:
    computer = "Schere"
    print(computer)
elif computer == 2:
    computer = "Stein"
    print(computer)
else:
    computer = "Papier"
    print(computer)

#Die möglichen Fälle vergleichen

if (p1 == "s" and computer == "Papier") or (p1 == "r" and computer == "Schere") or (p1 == "p" and computer == "Stein"):
    print("Player1 gewinnt!")
elif (p1 == "s" and computer == "Stein") or (p1 == "r" and computer == "Papier") or (p1 == "p" and computer == "Schere"):
    print("Computer gewinnt")
else:
    print("Unentschieden")

