diakok = []
osszeg = 0

for i in range(4):
    nev = input("Tanuló neve: ")
    kor = input("Életkor: ")

    diakok.append((nev, kor))
    osszeg += kor

print("Átlag életkor:", osszeg / 4)
