# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<                                                       >>>
# <<< 26_Számkitalálás_megoldva (Python gyakorlófeladat)    >>>
# <<<                                                       >>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
Készíts programot, amelyben a számítógép gondol egy számra, és a felhasználónak ki kell találni azt!

Feladatok:
a) A program véletlenszerűen válasszon ki egy számot 1 és 100 között (használj random modult)!

b) A felhasználó próbálja meg kitalálni a számot!
A program minden próbálkozás után jelezze:

hogy a tipp kisebb, vagy

nagyobb, mint a keresett szám.

c) A program csak akkor álljon le, ha a felhasználó el is találta a számot.

d) A játék végén írd ki, hány próbálkozás kellett a helyes tipphez!

Tippek:
Használd a random.randint(1, 100) függvényt!

A while ciklus tökéletes a „próbálkozás ismétlésére”.

Számlálj, hogy tudd, hányszor próbálkozott a játékos.

"""
import random

# Véletlen szám generálása
gondolt_szam = random.randint(1, 100)
tipp = None
probalkozasok = 0

print("Gondoltam egy számra 1 és 100 között. Találd ki!")

while tipp != gondolt_szam:
    try:
        tipp = int(input("Mi a tipped? "))
        if not 1 <= tipp <= 100:
            print("A számnak 1 és 100 között kell lennie!")
            continue
        probalkozasok += 1

        if tipp < gondolt_szam:
            print("Túl kicsi!")
        elif tipp > gondolt_szam:
            print("Túl nagy!")
        else:
            print(f"Gratulálok! Eltaláltad {probalkozasok} próbálkozás után.")
    except ValueError:
        print("Kérlek, számot adj meg!")
