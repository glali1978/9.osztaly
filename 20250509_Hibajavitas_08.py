napok = 3
meresek_szama = 4
adatok = []

for nap in range(napok):
    print("Nap", nap + 1)
    napi = []
    for m in range(meresek_szama)
        ertek = input("Hőmérséklet: ")
        napi.append(ertek)
    adatok.append(napi)

print("Napi átlagok:")
for nap in adatok:
    atlag = sum(nap) / len(nap)
    print("Átlag:", atlag)
