vasarlok = []

for i in range(3):
    nev = input("Vásárló neve: ")
    termekek = []

    print("Írj be termékeket (kesz a befejezéshez)")
    termek = input("Termék: ")
    while termek != "kesz":
        if len(termek) > 0
            termekek.append(termek)
        else:
            print("Üres termék nem lehet!")

        input("Következő termék: ")

    vasarlok.append((nev, termekek))

print("Összes vásárló és termékei:")
for vasarlo in vasarlok:
    print("Név:", vasarlo[0])
    for i in range(len(vasarlo[1])):
        print(i+1, ". ", vasarlo[1][i].upper)
