filmlista = []

for i in range(3)
    nev = input("Diák neve: ")
    filmek = []
    for j in range(2):
        film = input("Kedvenc filmed: ")
        if len(film) == 0
            print("Nem adhatsz meg üres filmet!")
        else:
            filmek.append(film)
    
    filmlista.append(nev, filmek)

print("Diákok filmjei:")
for adat in filmlista:
    print(adat[0] + ":")
    for f in filmek:
        print("-", f)
