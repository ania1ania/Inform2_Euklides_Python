
def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


def rzad(goscie, gospodarze):
	return nwd(goscie, gospodarze)

print("")
print("Wyniki testów:")
print(" Test           | Oczekiwano | Otrzymano | Wynik")
print("----------------+------------+-----------+-----------")
print(" rzad(100, 100) | 100        | ", rzad(100, 100),"     |")
print("----------------+------------+-----------+-----------")
print(" rzad(51, 65)   | 1          | ", rzad(51, 65),"       |")
print("----------------+------------+-----------+-----------")
print(" rzad(32, 48)   | 16         | ", rzad(32, 48),"      |")
