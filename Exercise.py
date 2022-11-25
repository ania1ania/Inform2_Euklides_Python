
def ile_cyfr(liczba):
    l_cyfr = 0
    while liczba > 0:
        liczba //= 10
        l_cyfr += 1
    return l_cyfr

print("Powinno być 3 jest", ile_cyfr(123))
print("Powinno być 5 jest", ile_cyfr(17923))
print("Powinno być 9 jest", ile_cyfr(179233334))
print("Powinno być 1 jest", ile_cyfr(1))
