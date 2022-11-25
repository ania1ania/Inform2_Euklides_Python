
import CheckIt

def sumap(lista):
    sum = 0
    for x in lista:
        if x == 0:
            break
        if (x % 2) == 0:
            sum += x
    return sum

print("")
print("Wyniki testów:")
print("----------------------------------+------------+-----------+-----------")
print(" Test                             | Oczekiwano | Otrzymano | Wynik")
print("----------------------------------+------------+-----------+-----------")
print(" sumap([2, 4, 11, 6, 5, 0, 7, 6]) | 12         | ", sumap([2, 4, 11, 6, 5, 0, 7, 6]),"      |", CheckIt.checkIt(12, sumap([2, 4, 11, 6, 5, 0, 7, 6])))
print("----------------------------------+------------+-----------+-----------")
print(" sumap([1, 1, 0, 1, 1, 6])        | 0          | ", sumap([1, 1, 0, 1, 1, 6]),"       |", CheckIt.checkIt(0, sumap([1, 1, 0, 1, 1, 6])))
print("----------------------------------+------------+-----------+-----------")
print(" sumap([0])                       | 0          | ", sumap([0]),"       |", CheckIt.checkIt(0, sumap([0])))
print("")
