def NWD(a, b):
    if b != 0:
        return NWD(b, a % b)
    return a

liczba_a = int(input("Podaj pierwszą liczbę naturalną: "))
liczba_b = int(input("Podaj drugą liczbę naturalną: "))

print("Największy wspólny dzielnik to:", NWD(liczba_a,liczba_b))