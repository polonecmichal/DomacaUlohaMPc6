def p_n(z):
    parne = []
    neparne = []
    for cislo in z:
        if cislo % 2 == 0:
            parne.append(cislo)
        else:
            neparne.append(cislo)
    return("parne su:", parne, "neparne su:", neparne)
