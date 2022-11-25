
import CheckIt

def suma(lista):
    sum = 0
    for x in lista:
        if x == 0:
            break
        sum += x
    return sum

print("")
print("Wyniki testów:")
print(" Test                                 | Oczekiwano | Otrzymano | Wynik")
print("--------------------------------------+------------+-----------+-----------")
print(" suma([2, 4, 11, 6, 5, 0, 7, 6])      | 28         | ", suma([2, 4, 11, 6, 5, 0, 7, 6]),"      |", CheckIt.checkIt(28, suma([2, 4, 11, 6, 5, 0, 7, 6])))
print("--------------------------------------+------------+-----------+-----------")
print(" suma([1, 1, 0, 1, 1, 6])             | 2          | ", suma([1, 1, 0, 1, 1, 6]),"       |", CheckIt.checkIt(2, suma([1, 1, 0, 1, 1, 6])))
print("--------------------------------------+------------+-----------+-----------")
print(" suma([0])                            | 0          | ", suma([0]),"       |", CheckIt.checkIt(0, suma([0])))
print("")
