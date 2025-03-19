"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<                                                       >>>
<<< Hőmérsékleti adatok elemzése (Python gyakorlófeladat) >>>
<<<                                                       >>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Feladatleírás
Készíts programot, amely egy hét napi hőmérsékleti adatait kéri be, majd elemezi azokat!

Feladatok
a) A program kérje be, hány nap hőmérsékletét szeretnéd rögzíteni. (NEM KÖTELEZŐ:while ciklus hogy csak érvényes, számot fogadjon el!)
b) Egy for ciklusban kérje be a napi hőmérsékleteket Celsius fokban, és tárolja el egy listában.
c) Minden új adat megadása után írja ki az eddigi adatokat.
d) A végén számolja ki és írja ki:
A legmagasabb és legalacsonyabb hőmérsékletet
Az átlaghőmérsékletet két tizedesre kerekítve
A hőmérsékleteket növekvő sorrendben

Extra feladat(nem kötelező):
Ha a felhasználó rossz formátumú számot ad meg (pl. szöveget ír be), a program ne omoljon össze, hanem kérjen új adatot!
Ne lehessen irreális értékeket megadni (pl. -1000 vagy 1000 °C)." 


Tipp a megoldáshoz
"°" karakter beírása = [ALT]+[0176]
a) A while ciklus biztosítja, hogy a felhasználó csak érvényes egész számot adjon meg a napok számához.
b) A for ciklusban a hőmérsékleteket egy listában tároljuk.
c) A print() segítségével minden új adat után kiírjuk az eddigi értékeket.
d) A min() és max() függvények kiszámolják a szélsőértékeket.
e) Az átlagot a sum(lista) / len(lista) kifejezéssel kapjuk meg.
f) A rendezéshez használjuk a sorted(lista) függvényt.

"""
# Üres lista a hőmérsékletek tárolására

# Bekérjük, hány nap hőmérsékletét kell megadni (while ciklus a helyes inputért)

# For-ciklussal bekérjük az adatokat
  # Életszerű határok ellenőrzése -50 +50

    # Eddigi hőmérsékletek kiíratása

# Eredmények kiíratása
print("\nEredmények:")
#"Legalacsonyabb hőmérséklet: 
#"Legmagasabb hőmérséklet: 
#"Átlaghőmérséklet: 
#"Hőmérsékletek növekvő sorrendben:
