cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parne = []
neparne = []
for cislo in cisla:
    if cislo % 2 == 0:
        parne.append(cislo)
    else:
        neparne.append(cislo)
print("parne su:", parne, "neparne su:", neparne)
