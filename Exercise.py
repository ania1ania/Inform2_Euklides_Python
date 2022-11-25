
import CheckIt

def sumanp(lista):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass

print("")
print("Wyniki testów:")
print("----------------------------------+------------+-----------+-----------")
print(" Test                             | Oczekiwano | Otrzymano | Wynik")
print("----------------------------------+------------+-----------+-----------")
print(" sumanp([2, 4, 11, 6, 5, 0, 7, 6])| 16         | ", sumanp([2, 4, 11, 6, 5, 0, 7, 6]),"      |", CheckIt.checkIt(16, sumanp([2, 4, 11, 6, 5, 0, 7, 6])))
print("----------------------------------+------------+-----------+-----------")
print(" sumanp([1, 1, 0, 1, 1, 6])       | 2          | ", sumanp([1, 1, 0, 1, 1, 6]),"       |", CheckIt.checkIt(2, sumanp([1, 1, 0, 1, 1, 6])))
print("----------------------------------+------------+-----------+-----------")
print(" sumanp([0])                      | 0          | ", sumanp([0]),"       |", CheckIt.checkIt(0, sumanp([0])))
print("")
