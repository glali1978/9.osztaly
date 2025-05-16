"""
<<< 2025.05.16 01.FELADAT >>>

a, Hozz létre egy üres listát, amelyben számokat fogsz tárolni!
b, Kérj be a felhasználótól 5 egész számot!
c, Minden bevitt számot adj hozzá a listához!
d, A bekérés után írasd ki a listát a képernyőre!
e, Írasd ki a listában szereplő számok összegét is!

"""
#  Üres lista létrehozása
szamok = []

# 5 szám bekérése a felhasználótól
for i in range(5):
    szam = int(input())
    szamok.append(szam)  # Szám hozzáadása a listához

# Lista kiíratása
print("A megadott számok:", szamok)

# Számok összege
osszeg = sum(szamok)
print("A számok összege:", osszeg)
