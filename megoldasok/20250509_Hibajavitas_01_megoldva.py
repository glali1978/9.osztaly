legjobb_atlag = 0
legjobb_diak = ""

for i in range(3):
    nev = input("Tanuló neve: ")
    jegyek = []

    for j in range(3):
        jegy = int(input(f"Add meg a(z) {j+1}. jegyet: "))
        jegyek.append(jegy)

    atlag = sum(jegyek) / len(jegyek)

    print("Tanuló:", nev, "| Átlag:", round(atlag, 2))

    if atlag > legjobb_atlag:
        legjobb_atlag = atlag
        legjobb_diak = nev

print("Legjobb tanuló:", legjobb_diak, "átlag:", round(legjobb_atlag, 2))
