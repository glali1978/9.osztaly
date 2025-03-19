"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<                                                       >>>
<<< Személyek adatai listában    (Python gyakorlófeladat) >>>
<<<                                                       >>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Készíts egy Python programot, amely egy listákból álló listában tárolja különböző személyek adatait (név, életkor, lakcím). A program a következőket tudja:

Új személy hozzáadása a listához.
A legfiatalabb személy keresése és kiírása.
A legidősebb személy keresése és kiírása.
A lakcímek listájának kiírása minden egyes személy neve mellett.
Az összes személy kiírása (név, életkor, lakcím).


"""
# Személyek listája: minden személy egy listába van mentve (név, életkor, lakcím)
szemelyek = [
    ["József", 25, "Budapest, Fő utca 1."],
    ["Anna", 30, "Debrecen, Kossuth tér 2."],
]

# 1. Új személy hozzáadása
def uj_szemely():


# 2. Legfiatalabb személy keresése
def legfiatalabb():
    fiatal = min(szemelyek, key=lambda x: x[1])
    print(f"A legfiatalabb személy: {fiatal[0]}, {fiatal[1]} éves, lakcím: {fiatal[2]}.")

# 3. Legidősebb személy keresése
def legidosebb():

# 4. Lakcímek listájának kiírása
def lakcimek()

# 5. Az összes személy kiírása
def szemelyek_lista():
    for szemely in szemelyek:
        print(f"{szemely[0]}, {szemely[1]} éves, lakcím: {szemely[2]}")

# Program indítása
print("Kezdő személyek:")
szemelyek_lista()

# Funkciók tesztelése
uj_szemely()
legfiatalabb()
legidosebb()
lakcimek()
szemelyek_lista()