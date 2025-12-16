z = [5,1,2,4,7,8,11]

def parne_pozicie(z):
    lok_zoznam = []
    for i in range(0, len(z), 2):
        lok_zoznam.append(z[i])
    return lok_zoznam
