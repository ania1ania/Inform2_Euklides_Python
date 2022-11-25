
def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


def kiedy(x, y):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass

print("")
print("Wyniki testów:")
print(" Test           | Oczekiwano | Otrzymano | Wynik")
print("----------------+------------+-----------+-----------")
print(" kiedy(2, 5)    | 10         | ", kiedy(2, 5),"       |")
print("----------------+------------+-----------+-----------")
print(" kiedy(3, 3)    | 3          | ", kiedy(3, 3),"        |")
print("----------------+------------+-----------+-----------")
print(" kiedy(4, 7)    | 28         | ", kiedy(4, 7),"       |")
