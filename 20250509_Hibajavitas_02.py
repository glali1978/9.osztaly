kolcsonzesek = []

for i in range(3):
    nev = input("Olvasó neve: ")
    konyv = input("Kölcsönzött könyv címe: ")
    napok = input("Kölcsönzési napok száma: ")

    kolcsonzesek.append((nev, konyv, napok))

print("Kölcsönzési adatok:")
for adat in kolcsonzesek:
    print(f"{adat[0]} kölcsönözte: {konyv} ({napok} napra)")
