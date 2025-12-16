z = ['ahoj', 12, -3, 'kukuk', 6.45, True]

def parne_pozicie(z):
    lok_zoznam = []
    for i in range(0, len(z), 2):
        lok_zoznam.append(z[i])
    return lok_zoznam
