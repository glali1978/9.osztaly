#
# 22_Hibajavitas_megoldva
#

"""
Kérj be a felhasználótól egész számokat addig, amíg nullát nem ír.
Ezután írd ki:
  - a megadott számok listáját
  - az összegüket
  - és az átlagukat
"""

szamok = []
szam = 1

while szam != 0:
    szam = int(input("Adj meg egy számot (0 a kilépéshez): "))
    if szam != 0:
        szamok.append(szam)

print("Megadott számok:", szamok)

osszeg = 0
for s in szamok:
    osszeg = osszeg + s

print("Összeg:", osszeg)

atlag = osszeg / len(szamok)
print("Átlag:", atlag)