#
# 24_Hibajavitas_feladat
#
"""
A felhasználó termékeket adhat hozzá a bevásárlólistához.
A program akkor áll le, ha a felhasználó azt írja be: „kesz”.

A végén írjuk ki az összes terméket nagybetűsen, számozva.
"""

lista = []

termek = input("Adj meg egy terméket ('kesz' a kilépéshez): ")

while termek != "kesz":
    if len(termek) > 0
        lista.append(termek)
    else
        print("Üres termék nem lehet!")

    input("Következő termék: ")

print("Bevásárlólista:")

for i in range(lista):
    print(f"{i+1}. {lista[i].upper}")
