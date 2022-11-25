
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

def kiedy(x, y):
    return nww(x, y)

print("")
print("Wyniki testów:")
print(" Test           | Oczekiwano | Otrzymano | Wynik")
print("----------------+------------+-----------+-----------")
print(" kiedy(2, 5)    | 10         | ", kiedy(2, 5),"      |", checkIt(10, kiedy(2, 5)))
print("----------------+------------+-----------+-----------")
print(" kiedy(3, 3)    | 3          | ", kiedy(3, 3),"       |", checkIt(3, kiedy(3, 3)))
print("----------------+------------+-----------+-----------")
print(" kiedy(4, 7)    | 28         | ", kiedy(4, 7),"      |", checkIt(28, kiedy(4, 7)))

