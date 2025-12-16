z = ['ahoj', 12, -3, 'kukuk', 6.45, True]

def len_cisla(z):
    lok_list = []
    for vec in z:
        if isinstance(vec, (int, float)):
            lok_list.append(vec)
    return lok_list
