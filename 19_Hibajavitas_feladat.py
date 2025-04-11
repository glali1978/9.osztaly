#
# 19_Hibajavitas_feladat
#

"""
A. Döntsd el, hogy a szám pozitív, negatív vagy nulla!
"""

szam = -3

if szam < 0
    print("A szám pozitív.")
elif szam > 0
    print("A szám negatív.")
else:
    print("A szám nulla.")


"""
B. Vizsgáld meg, hogy a felhasználó által megadott kor alapján nagykorú-e!
"""

kor = input("Hány éves vagy? ")

if kor >= 18:
    print("Nagykorú vagy.")
else:
    print("Kiskorú vagy.")


"""
C. Kérj be egy színt, és írd ki, hogy benne van-e a kedvenc színek listában!
"""

kedvenc_szinek = ["piros", "kék", "zöld"]
szin = input("Mondj egy színt: ")
if szin.lower in kedvenc_szinek:
    print("Ez egy kedvenc szín!")
else:
    print("Ez nem egy kedvenc szín.")