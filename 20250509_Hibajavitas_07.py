nevek = []
allatok = []

nev = ""
while nev != "stop":
    nev = input("Név: ")
    if nev == "stop":
        break
    nevek.append(nev)

    allat = input("Kedvenc állat: ")
    if len(allat) > 0
        allatok.append(allat)
    else:
        allatok.append("nincs megadva")

print("Eredmény:")
for i in range(len(nevek)):
    print(nevek[i] + " kedvenc állata:" allatok[i])
