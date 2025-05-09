diakok = []
osszeg = 0

for i in range(4):
    nev = input("Tanuló neve: ")
    kor = int(input("Életkor: "))

    diakok.append((nev, kor))
    osszeg += kor

print("Átlag életkor:", round(osszeg / len(diakok), 2))
