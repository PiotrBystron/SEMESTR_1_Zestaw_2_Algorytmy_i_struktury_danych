def silnia_for(liczba):
    ile = 0
    s = 1
    for i in range(2, liczba+1):
        ile +=1
        s = s * i
    return s, ile

liczba = int(input("Podaj liczbę naturalną do obliczenia silni: "))

print("Silnia z podanej liczy oraz ilość mnożeń", silnia_for(liczba))
#print(liczba , "! to:", silnia_for(liczba))