
def checkIt(a, b):
    if a == b:
        return "Pozytywny"
    else:
        return "Negatywny"

def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a

def nww(a, b):
    return (a * b) // nwd(a, b)

def flamastry(x, y, z):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass

print("")
print("Wyniki testów:")
print(" Test                  | Oczekiwano | Otrzymano | Wynik")
print("-----------------------+------------+-----------+-----------")
print(" flamastry(5, 110, 15) | 22         | ", flamastry(5, 110, 15),"      |", checkIt(22, flamastry(5, 110, 15)))
print("-----------------------+------------+-----------+-----------")
print(" flamastry(5, 10, 15)  | 2          | ", flamastry(5, 10, 15),"       |", checkIt(2, flamastry(5, 10, 15)))
print("-----------------------+------------+-----------+-----------")
print(" flamastry(7, 9, 7)    | 9          | ", flamastry(7, 9, 7),"       |", checkIt(9, flamastry(7, 9, 7)))
