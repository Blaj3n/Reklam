# print("1. feladat")

rendelesek = []
with open("rendel.txt", "r", encoding="utf-8") as file:
    for rendel in file:
        rendel = rendel.strip().split()
        rendelesek.append([int(rendel[0]), str(rendel[1]), int(rendel[2])])
print(rendelesek)
