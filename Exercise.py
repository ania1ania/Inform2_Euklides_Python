
import CheckIt

def iledo6(lista):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass

print("")
print("Wyniki testów:")
print(" Test                                 | Oczekiwano | Otrzymano | Wynik")
print("--------------------------------------+------------+-----------+-----------")
print(" iledo6([6])                          | 0          | ", iledo6([6]),"       |", CheckIt.checkIt(0, iledo6([6])))
print("--------------------------------------+------------+-----------+-----------")
print(" iledo6([1, 1, 1, 1, 5, 6, 6, 6, 6])  | 5          | ", iledo6([1, 1, 1, 1, 5, 6, 6, 6, 6]),"       |", CheckIt.checkIt(5, iledo6([1, 1, 1, 1, 5, 6, 6, 6, 6])))
print("--------------------------------------+------------+-----------+-----------")
print(" iledo6([0, 0, 0, 0, 6])              | 4          | ", iledo6([0, 0, 0, 0, 6]),"       |", CheckIt.checkIt(4, iledo6([0, 0, 0, 0, 6])))
