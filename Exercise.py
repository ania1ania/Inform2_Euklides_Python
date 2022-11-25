
import CheckIt

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma

print("")
print("Wyniki testów:")
print(" Test                  | Oczekiwano | Otrzymano | Wynik")
print("-----------------------+------------+-----------+-----------")
print(" suma_cyfr(12)         | 3          | ", suma_cyfr(12),"       |", CheckIt.checkIt(3, suma_cyfr(12)))
print("-----------------------+------------+-----------+-----------")
print(" suma_cyfr(179233334)  | 35         | ", suma_cyfr(179233334),"      |", CheckIt.checkIt(35, suma_cyfr(179233334)))
print("-----------------------+------------+-----------+-----------")
print(" suma_cyfr(1)          | 1          | ", suma_cyfr(1),"       |", CheckIt.checkIt(1, suma_cyfr(1)))
