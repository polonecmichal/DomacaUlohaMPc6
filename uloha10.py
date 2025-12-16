z = [4, 1, 5, 27, -7,12] 

def maxx(z)(z):
    maximum = z[0]
    for cislo in z[::1]:
        if cislo > maximum:
            maximum = cislo 
            
    return maximum
