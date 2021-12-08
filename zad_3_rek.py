def silnia_rek(liczba):
    if liczba < 1:
        return 1
    #else:
    #    return liczba * silnia_rek(liczba - 1)
    return liczba * silnia_rek(liczba - 1)

liczba = int(input("Podaj liczbę naturalną do obliczenia silni: "))

print(liczba, "! to:", silnia_rek(liczba))