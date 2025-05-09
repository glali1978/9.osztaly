# Helyes bevásárlólista program

vasarlok = []

for i in range(3):
    nev = input("Vásárló neve: ")
    termekek = []

    print("Írj be termékeket (kesz a befejezéshez)")
    while True:
        termek = input("Termék: ")
        if termek == "kesz":
            break
        elif len(termek) > 0:
            termekek.append(termek)
        else:
            print("Üres termék nem lehet!")

    vasarlok.append((nev, termekek))

print("\nÖsszes vásárló és termékei:")
for vasarlo in vasarlok:
    print("\nNév:", vasarlo[0])
    for i in range(len(vasarlo[1])):
        print(f"{i+1}. {vasarlo[1][i].upper()}")
