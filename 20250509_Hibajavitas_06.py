naplo = []

for nap in range(3)
    print("Nap:", nap + 1)
    esemenyek = []

    while True:
        esemeny = input("Esemény: ")
        if esemeny == "kesz":
            break
        elif len(esemeny) == 0:
            print("Üres bejegyzés!")
        else
            esemenyek.append(esemeny)

    naplo.append(esemenyek)

print("Teljes napló:")
for i in range(3):
    print("Nap", i + 1)
    for j in range(len(naplo[i])):
        print(j + 1, ".", naplo[i][j])
