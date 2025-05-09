legjobb_atlag = 0
legjobb_diak = ""

for i in range(3):
    nev = input("Tanuló neve: ")
    jegyek = []

    for j in range(3):
        jegy = input("Add meg a(z)" j+1 ". jegyet: ")
        jegyek.append(jegy)

    atlag = sum(jegyek) / 3

    print("Tanuló:", nev, "| Átlag:", atlag)

    if atlag > legjobb_atlag:
        legjobb_atlag = atlag
        legjobb_diak = nev

print("Legjobb tanuló:" legjobb_diak, "átlag:", legjobb_atlag)
