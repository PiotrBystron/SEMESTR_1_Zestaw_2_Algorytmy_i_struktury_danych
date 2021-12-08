def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

liczba_a = int(input("Podaj pierwszą liczbę naturalną: "))
liczba_b = int(input("Podaj drugą liczbę naturalną: "))

print("Największy wspólny dzielnik to:", NWD(liczba_a,liczba_b))