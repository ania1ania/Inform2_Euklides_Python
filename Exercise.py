
import CheckIt

def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a

def nww(a, b):
    return (a * b) // nwd(a, b)

def flamastry(x, y, z):
    pom1 = nww(x, y)
    pom2 = nww(pom1, z)
    return pom2 // z

print("")
print("Wyniki testów:")
print(" Test                  | Oczekiwano | Otrzymano | Wynik")
print("-----------------------+------------+-----------+-----------")
print(" flamastry(5, 110, 15) | 22         | ", flamastry(5, 110, 15),"      |", CheckIt.checkIt(22, flamastry(5, 110, 15)))
print("-----------------------+------------+-----------+-----------")
print(" flamastry(5, 10, 15)  | 2          | ", flamastry(5, 10, 15),"       |", CheckIt.checkIt(2, flamastry(5, 10, 15)))
print("-----------------------+------------+-----------+-----------")
print(" flamastry(7, 9, 7)    | 9          | ", flamastry(7, 9, 7),"       |", CheckIt.checkIt(9, flamastry(7, 9, 7)))
