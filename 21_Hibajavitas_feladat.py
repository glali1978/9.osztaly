#
# 21_Hibajavitas_feladat
#

"""
Kérj be a felhasználótól egy számot, majd számolj vissza 1-ig.
"""

szam = input("Adj meg egy számot: ")

while szam > 0
    print(szam)
    szam = szam - 1
print("Visszaszámlálás kész!")


"""
Kérj be 5 nevet, és írd ki őket nagybetűsen.
"""

nevek = []

for i in range(5)
    nev = input("Adj meg egy nevet: ")
    nevek append(nev)

print("A megadott nevek:")
for nev in nevek
    print(nev.upper)