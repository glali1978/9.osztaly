"""

<<< 2025.05.16 3.FELADAT >>>

a,Hozz létre egy üres listát, amelyben neveket fogsz tárolni!
b,Kérj be a felhasználótól tetszőleges számú nevet!
  Ha a felhasználó üres sort ad meg (csak Enter-t nyom), akkor a bevitel befejeződik.
  A bekérés után:
c,Írasd ki a lista tartalmát!
d,Írasd ki, hogy hány nevet adott meg a felhasználó!
e,Írasd ki a neveket ábécé sorrendben!
f,Keresd meg a leghosszabb nevet és írasd ki!

"""
# Üres lista létrehozása
nevek = []

# Nevek bekérése a felhasználótól
while True:
    nev = input("Adj meg egy nevet (vagy nyomj Entert a befejezéshez): ")
    if nev == "":  # Ha üres sort ad meg, kilép a ciklusból
        break
    nevek.append(nev)  # Név hozzáadása a listához

# Lista kiíratása
print("\nMegadott nevek:", nevek)

# Nevek számának kiírása
print(f"Összesen {len(nevek)} nevet adtál meg.")

# Nevek ábécé sorrendben
print("Nevek ábécé sorrendben:", sorted(nevek))

# Leghosszabb név keresése
if nevek:  # Csak akkor keresünk, ha van legalább egy név a listában
    leghosszabb = max(nevek, key=len)
    print("A leghosszabb név:", leghosszabb)
