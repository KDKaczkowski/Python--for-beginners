'''
Napisz dekorator @is_correct,  który opakowuje funkcję zwracającą słownik. 
Dekorator ma sprawdzić czy w słowniku znajdują się klucze zawarte w argumentach dekoratora. 
Jeśli tak niech zwróci ten słownik, jeśli nie, niech zwraca wartość None.


'''



def is_correct(*args):
  def check(func):
      def wrap():
        dictt = func()
        for arg in args:
          if arg not in dictt:
            return None
        return dictt
      return wrap
  return check
  pass
'''
Napisz dekorator @add_date,  który opakowuje funkcję zwracającą słownik. 
 Dekorator ma dodać aktualną datę do zwracanego przez dekorowaną funkcję słownika w formacie podanym jako argument dekoratora.

Użyj modułu datetime korzystając z datetime.datetime.now() do pobrania aktualnej daty. 
Więcej informacji o formatowaniu znajdziesz tutaj:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
import datetime  # do not change this import, use datetime.datetime.now() to get date
from functools import wraps

def add_date(format):
  def dekorator(func):
    @wraps(func)
    def dodaj():
      dictt = func()
      time = datetime.datetime.now()
      b = time.strftime(format)
      dictt.update({'date' : b})
      return dictt
    return dodaj
  return dekorator
  '''
Napisz dekorator @to_list,  który opakowuje funkcję zwracającą tekst (iterable) 
oraz zwraca jej znaki (elementy) w postaci jednowymiarowej listy.
  '''
  def to_list(func):
  def split():
    return list(func())
  return split
