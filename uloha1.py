import random

def generuj(n):
    zoznam = []
    for i in range(n):
        cislo = random.randint(5, 10)
        zoznam.append(cislo)
    return zoznam
