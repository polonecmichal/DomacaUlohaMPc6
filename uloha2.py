def sucet_parne(z):
    sucet = 0
    for cislo in z:
        if cislo % 2 == 0:
            sucet += cislo
            
    return sucet
