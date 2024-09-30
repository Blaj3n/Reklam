hello = ["h", "e", "l", "l", "o"]

# ha az érettségi feladat megköveteli tőlünk, hogy minden egyes max elemet írjunk ki index szerint:

print("1: ")
for index, betu in enumerate(hello): # az index == adott listaelem indexével, betu (bármilyen nevet adhatunk) == elem, [{0: "h"}, {1: "e"}, {2: "l"}, {3: "l"}, {4: "o"}]
    if betu == "l":
        print(f"l indexe: {index}")

# Ez az index [ nagy_halmaz (lista).INDEX(a keresett elem) ] az éretségi feladatokban úgy jelenik meg, ha például egy dologra vagyunk kiváncsiak, "például a 9. napon volt a sűrű a rendelés"

print("2: ")
e_betu_indexe = hello.index("l")
print(e_betu_indexe)