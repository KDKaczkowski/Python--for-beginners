#Zadanie 2
#Napisz funkcję reduce.
#Funkcja ma na celu sumowanie kolejnych par elementów zadanej listy i zwrócenie listy sum kolejnych par.
#Jeżeli lista ma nieparzystą długość, ostatni element zostaje przepisany od listy wynikowej na ostatniej pozycji.

# zadanie 2

def reduce(lista):
  x = len(lista)
  if x % 2 == 0:
    for n in range(0, x-1, 2):
      lista[int(n / 2)] = lista[n] + lista[n + 1]
    del lista[int(x/2):x]
    return lista
  else:
    for n in range(0, x - 2, 2):
      lista[int(n / 2)] = lista[n] + lista[n + 1]
    lista[int(x / 2)] = lista[x - 1]
    del lista[int(x / 2 + 1):x]
    return lista


assert reduce([1, 2, 3, 4, 5, 6]) == [3, 7, 11]
assert reduce([1, 2, 3, 4, 5, 6, 7]) == [3, 7, 11, 7]
