def NWD(a, b):
    if a != b:
        if a > b:
            return NWD(a-b, b)
        else:
            return NWD(b-a, a)
    return a

liczba_a = int(input("Podaj pierwszą liczbę naturalną: "))
liczba_b = int(input("Podaj drugą liczbę naturalną: "))

print("Największy wspólny dzielnik to:", NWD(liczba_a,liczba_b))