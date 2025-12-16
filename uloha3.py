def coho_je_viac(z):
    pocet_parne = 0
    pocet_neparne = 0
    
    for cislo in z:
        
        if cislo % 2 == 0:
            pocet_parne += 1
        else:
            pocet_neparne += 1
        
    if pocet_parne > pocet_neparne:
        return 'parne'
    elif pocet_neparne > pocet_parne:
        return 'neparne'
    else:
        return 'rovnako'
