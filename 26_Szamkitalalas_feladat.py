# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<                                                       >>>
# <<< 26_Számkitalálás_feladat (Python gyakorlófeladat)     >>>
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


