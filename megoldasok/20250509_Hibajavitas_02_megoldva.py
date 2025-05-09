kolcsonzesek = []

for i in range(3):
    nev = input("Olvasó neve: ")
    konyv = input("Kölcsönzött könyv címe: ")
    napok = int(input("Kölcsönzési napok száma: "))

    kolcsonzesek.append((nev, konyv, napok))

print("Kölcsönzési adatok:")
for adat in kolcsonzesek:
    print(f"{adat[0]} kölcsönözte: {adat[1]} ({adat[2]} napra)")
