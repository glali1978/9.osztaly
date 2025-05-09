termekek = []
vegosszeg = 0

for i in range(3):
    nev = input("Termék neve: ")
    ar = int(input("Ár: "))

    termekek.append((nev, ar))
    vegosszeg += ar

print("Összesen fizetendő:", vegosszeg, "Ft")
