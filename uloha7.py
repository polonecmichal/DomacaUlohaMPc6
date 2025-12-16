zoznam_mocniny = [1,2,3,4,5,6,7,8,9,10]
def zoznam_mocnin(n):
    lokalny_list = []
    for cisla in zoznam_mocniny:
        lokalny_list.append(cisla ** 2)
    return lokalny_list
