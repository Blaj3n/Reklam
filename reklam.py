# print("1. feladat")
rendelesek = []
with open("rendel.txt", "r", encoding="utf-8") as file:
    for rendel in file:
        rendel = rendel.strip().split()
        rendelesek.append([int(rendel[0]), str(rendel[1]), int(rendel[2])])
print(rendelesek)


print("2. feladat: ")
# print(f"A rendelések száma: {len(rendelesek)}")
ossz_rendeles = 0
for rendel in rendelesek:
    ossz_rendeles += 1
print("A rendelések száma:", ossz_rendeles)


print("3. feladat: ")

megadott_nap = 3    # int(input("Kérem, adjon meg egy napot: "))

adott_nap_csomagszam = 0
for rendel in rendelesek:
    if rendel[0] == megadott_nap:
        adott_nap_csomagszam += 1
print(f"A rendelések száma az adott napon: {adott_nap_csomagszam}")


print("4. feladat: ")
osszes_nap = []

for nap in rendelesek:
    if nap[0] not in osszes_nap:
        osszes_nap.append(nap[0])
# print(osszes_nap)

szures = []

for nap in osszes_nap:
    for rendel in rendelesek:
        if rendel[0] == nap and rendel[1] == "NR" and nap not in szures:
            szures.append(nap)
# print(szures)
nincs_rendeles = len(osszes_nap) - len(szures)
if len(osszes_nap) != len(szures):
    print(f"{nincs_rendeles} nap nem volt a reklámban nem érintett városból rendelés")
elif nincs_rendeles == 0:    # elif len(osszes_nap) == len(szures):
    print("Minden nap volt rendelés a reklámban nem érintett városból")

print("5. feladat: ")

darabszamok = []
for rendel in rendelesek:
    darabszamok.append(rendel[2])
# print(darabszamok)
# print(max(darabszamok))
max_darabszam = max(darabszamok)
# print(len(darabszamok), len(rendelesek))
indexe_a_max_darabszam = darabszamok.index(max_darabszam)   # miután a len(darabszamok) == len(rendel.txt) [971],
# így ha veszem a darabszam lista maximumát [9], akkor simán megvizsgálhatom, hogy az hanyadik indexet foglalja el
# a darabszam listában.    # indexe_a_max_darabszam == 714


print(f"A legnagyobb darabszám: {rendelesek[indexe_a_max_darabszam][2]}, a rendelés napja:"
      f"{rendelesek[indexe_a_max_darabszam][0]}")
# print(indexe_a_max_darabszam)


# print("6. feladat")
def osszes_2(varos_2: str, nap_2: int):
    szamlalo = 0
    for rendel in rendelesek:
        if rendel[0] == nap_2 and rendel[1] == varos_2:
            szamlalo += rendel[2]
    return szamlalo


def osszes(varos: str, nap: int):
    szamlalo = 0
    for rendel in rendelesek:
        if rendel[0] == nap and rendel[1] == varos:
            szamlalo += 1   # rendel[2] itt írtam át azt, hogy a számlálóhoz ne a rendel[2],
            # hanem 1 adódjon hozzá a lenti videóból merítve az ötletet, és bevált :)
    return szamlalo


print(osszes("PL", 2))

osszes_PL_21 = osszes_2("PL", 21)
osszes_TV_21 = osszes_2("TV", 21)
osszes_NR_21 = osszes_2("NR", 21)
print(f"7. feladat: \nA rendelt termékek darabszáma a 21. napon PL: {osszes_PL_21} TV: {osszes_TV_21}"
      f" NR: {osszes_NR_21}")

print("8. feladat")

elso_tiz_PL_adatok = []
elso_tiz_TV_adatok = []
elso_tiz_NR_adatok = []

masodik_tiz_PL_adatok = []
masodik_tiz_TV_adatok = []
masodik_tiz_NR_adatok = []

harmadik_tiz_PL_adatok = []
harmadik_tiz_TV_adatok = []
harmadik_tiz_NR_adatok = []

for nap in range(1, 11):
    elso_tiz_PL_adatok.append(osszes("PL", nap))
    elso_tiz_TV_adatok.append(osszes("TV", nap))
    elso_tiz_NR_adatok.append(osszes("NR", nap))

for nap in range(11, 21):
    masodik_tiz_PL_adatok.append(osszes("PL", nap))
    masodik_tiz_TV_adatok.append(osszes("TV", nap))
    masodik_tiz_NR_adatok.append(osszes("NR", nap))

for nap in range(21, 31):
    harmadik_tiz_PL_adatok.append(osszes("PL", nap))
    harmadik_tiz_TV_adatok.append(osszes("TV", nap))
    harmadik_tiz_NR_adatok.append(osszes("NR", nap))

# print(elso_tiz_PL_adatok)
# print(elso_tiz_TV_adatok)
# print(elso_tiz_NR_adatok)

elso_tiz_PL_total = sum(elso_tiz_PL_adatok)
elso_tiz_TV_total = sum(elso_tiz_TV_adatok)
elso_tiz_NR_total = sum(elso_tiz_NR_adatok)

# print(masodik_tiz_PL_adatok)
# print(masodik_tiz_TV_adatok)
# print(masodik_tiz_NR_adatok)

masodik_tiz_PL_total = sum(masodik_tiz_PL_adatok)
masodik_tiz_TV_total = sum(masodik_tiz_TV_adatok)
masodik_tiz_NR_total = sum(masodik_tiz_NR_adatok)

# print(harmadik_tiz_PL_adatok)
# print(harmadik_tiz_TV_adatok)
# print(harmadik_tiz_NR_adatok)

harmadik_tiz_PL_total = sum(harmadik_tiz_PL_adatok)
harmadik_tiz_TV_total = sum(harmadik_tiz_TV_adatok)
harmadik_tiz_NR_total = sum(harmadik_tiz_NR_adatok)

# print(f"Összes PL: {elso_tiz_PL_total}, Összes TV: {elso_tiz_TV_total}, Összes NR: {elso_tiz_NR_total}")

print("Napok\t1..10\t11..20\t21..30")
print(f"PL      {elso_tiz_PL_total}\t\t{masodik_tiz_PL_total}\t\t{harmadik_tiz_PL_total}")
print(f"TV      {elso_tiz_TV_total}\t\t{masodik_tiz_TV_total}\t\t{harmadik_tiz_TV_total}")
print(f"NR      {elso_tiz_NR_total}\t\t{masodik_tiz_NR_total}\t\t{harmadik_tiz_NR_total}")
