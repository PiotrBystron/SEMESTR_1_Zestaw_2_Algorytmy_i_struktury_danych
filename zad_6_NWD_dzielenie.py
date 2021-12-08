def NWD(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

liczba_a = int(input("Podaj pierwszą liczbę naturalną: "))
liczba_b = int(input("Podaj drugą liczbę naturalną: "))

print("Największy wspólny dzielnik to:", NWD(liczba_a,liczba_b))