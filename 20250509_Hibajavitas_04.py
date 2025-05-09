termekek = []
vegosszeg = 0

for i in range(3):
    nev = input("Termék neve: ")
    ar = input("Ár: ")

    termekek.append((nev, ar))
    vegosszeg += ar
