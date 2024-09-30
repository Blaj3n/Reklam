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

megadott_nap = 3 #int(input("Kérem, adjon meg egy napot: "))

adott_nap_csomagszam = 0
for rendel in rendelesek:
    if rendel[0] == megadott_nap:
        adott_nap_csomagszam += 1
print(f"A rendelések száma az adott napon: {adott_nap_csomagszam}")


# HÁZI: 7.-ig
# print("4. feladat: ")
# rendelt_nap = 0
# nem_rendelt_nap = 0
# for nap in range(1, 31):
#     if rendel[1] == "NR":
#         rendelt_nap += 1
#     else:
#         nem_rendelt_nap += 1
# print(f"{nem_rendelt_nap} nap nem volt a reklámban nem érintett városból rendelés")

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
indexe_a_max_darabszam = darabszamok.index(max_darabszam)   # miután a len(darabszamok) == len(rendel.txt) [971], így ha veszem a darabszam lista maximumát [9], akkor simán megvizsgálhatom, hogy az hanyadik indexet foglalja el a darabszam listában.    # indexe_a_max_darabszam == 714


print(f"A legnagyobb darabszám: {rendelesek[indexe_a_max_darabszam][2]}, a rendelés napja: {rendelesek[indexe_a_max_darabszam][0]}")
# print(indexe_a_max_darabszam)


# print("6. feladat")

def osszes(varos: str, nap: int):
    szamlalo = 0
    for rendel in rendelesek:
        if rendel[0] == nap and rendel[1] == varos:
            szamlalo += rendel[2]
    return szamlalo


osszes_PL_21 = osszes("PL", 21)
osszes_TV_21 = osszes("TV", 21)
osszes_NR_21 = osszes("NR", 21)
print(f"7. feladat: \nA rendelt termékek darabszáma a 21. napon PL: {osszes_PL_21} TV: {osszes_TV_21}"
      f" NR: {osszes_NR_21}")
