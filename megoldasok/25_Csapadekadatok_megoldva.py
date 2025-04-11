# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<                                                       >>>
# <<< 25_Csapadékadatok_megoldva (Python gyakorlófeladat)   >>>
# <<<                                                       >>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
Feladatleírás
Készíts programot, amely egy hét napi csapadékadatát (mm-ben) kéri be, majd elemezi azokat!

Feladatok
a) Kérdezd meg, hány nap csapadékadatait szeretné a felhasználó rögzíteni!

b) Egy for ciklussal kérd be az egyes napok csapadékértékeit (milliméterben), és tárold el egy listában.

c) Minden új adat után jelenítsd meg az eddigi értékeket!

d) A program a végén írja ki:

Mennyi volt a legtöbb és legkevesebb csapadék (mm-ben)?

Mennyi volt az átlagos csapadék mennyiség (két tizedesjegyre kerekítve)?

A csapadékadatokat növekvő sorrendben.
"""
csapadekok = []

# A napok számának bekérése
napok = int(input("Hány napi csapadékadatot szeretnél megadni? "))

# Csapadékadatok bekérése ciklusban
for i in range(1, napok + 1):
    adat = float(input(f"{i}. nap csapadékmennyisége (mm): "))
    csapadekok.append(adat)
print("Eddigi csapadékadatok:", ", ".join(map(str, csapadekok)))

# Eredmények kiírása
print("\nEredmények:")
print(f"Legkevesebb csapadék: {min(csapadekok)} mm")
print(f"Legtöbb csapadék: {max(csapadekok)} mm")
print(f"Átlagos csapadékmennyiség: {round(sum(csapadekok)/len(csapadekok), 2)} mm")
print("Csapadékadatok növekvő sorrendben:", ", ".join(map(str, sorted(csapadekok))))

