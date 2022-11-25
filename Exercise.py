
def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


def ile(goscie, gospodarze):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass

print("")
print("Wyniki testów:")
print(" Test           | Oczekiwano | Otrzymano | Wynik")
print("----------------+------------+-----------+-----------")
print(" ile(100, 100)  | 2          | ", ile(100, 100),"      |")
print("----------------+------------+-----------+-----------")
print(" ile(51, 65)    | 116        | ", ile(51, 65),"       |")
print("----------------+------------+-----------+-----------")
print(" ile(32, 48)    | 5          | ", ile(32, 48),"       |")
