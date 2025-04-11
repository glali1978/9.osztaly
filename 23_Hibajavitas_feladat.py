#
# 23_Hibajavitas_feladat
#
"""
Kérjük be a diákok dolgozatjegyeit (1-től 5-ig), amíg az „x” betűt nem írják.
A program számolja meg, hány elégségesnél rosszabb (1-es), közepes (3-as),
és jeles (5-ös) jegy szerepel.

A végén írjuk ki a jegyek listáját és a darabszámokat.
"""

jegyek = []

bekeres = input("Adj meg egy jegyet (vagy 'x' a kilépéshez): ")

while bekeres != "x":
    if int(bekeres) >= 1 and <= 5
        jegyek.append(bekeres)
    else:
        print("Hibás érték! Csak 1-5 közötti szám lehet.")

    bekeres = input("Következő jegy: ")

print("Megadott jegyek:"+ jegyek)

egyes = 0
kozepes = 0
jeles = 0

fo jegy in jegyek:
    if jegy == 1
        egyes = egyes + 1
    elif jegy = 3:
        kozepes += 1
    elif jegy == "5":
        jeles += 1

print("Elégtelenek száma:", egyes)
print("Közepesek száma:", kozepes)
print("Jelesek száma:", jeles)
