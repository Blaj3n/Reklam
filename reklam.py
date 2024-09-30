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
megadott_nap = int(input("Kérem, adjon meg egy napot: "))
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
print(osszes_nap)

szures = []

for nap in osszes_nap:
    for rendel in rendelesek:
        if rendel[0] == nap and rendel[1] == "NR" and nap not in szures:
            szures.append(nap)
print(szures)
nincs_rendeles = len(osszes_nap) - len(szures)
if len(osszes_nap) != len(szures):
    print(f"{nincs_rendeles} nap nem volt a reklámban nem érintett városból rendelés")
elif nincs_rendeles == 0:    # elif len(osszes_nap) == len(szures):
    print("Minden nap volt rendelés a reklámban nem érintett városból")

# print("5. feladat: ")
#
# legnagyobb_darabszam = 0
# for rendel in rendelesek:
#     if max(rendel[2]):
#
# print(f"A legnagyobb darabszám: {max(rendel[2])}, a rendelés napja: {rendel[0]}")

# print("6. feladat")
#
#
# def osszes(varos: str, sorszam: int):
#     return varos, sorszam
