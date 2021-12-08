def silnia_while(liczba):
    n = 1
    ile = 0
    while liczba != 1:
        ile +=1
        if liczba == 0:
            return 1
        n = n * liczba
        liczba = liczba - 1
    return n, ile

liczba = int(input("Podaj liczbę naturalną do obliczenia silni: "))

print("Silnia z podanej liczy oraz ilość mnożeń", silnia_while(liczba))
#print(liczba , "! to:", silnia_while(liczba))