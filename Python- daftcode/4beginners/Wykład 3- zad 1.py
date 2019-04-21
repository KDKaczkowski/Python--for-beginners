#Zadanie 1 wyklad 3
#W tym zadaniu zawsze będą poprawne dane.
#Nie ma potrzeby obsługiwania sytuacji wyjątkowych.

#Napisz klasę MyFraction.
#Ta klasa ma reprezentować ułamek.
#Ta klasa ma być mutowalna.#
#Ta klasa ma mieć dwa pola: `numerator` i `denominator`.

#Instancję klasy powinno dać się utworzyć na następujące sposoby:
#  MyFraction(1, 2)
#  MyFraction(1, denominator=2)
#  MyFraction(numerator=1, denominator=2)
#  MyFraction(5) == MyFraction(5, 1)
#  MyFraction(numerator=6) == MyFraction(numerator=6, denominator=1)
#  MyFraction(MyFraction(1, 2)) == MyFraction(1, 2)

#Dodatkowo mianownik ułamka powinien zawsze być najmniejszą możliwą liczbą.
#Przykład:
#  a = MyFraction(10, 30)
#  assert 1 == a.numerator
#  assert 3 == a.denominator

#Ułamki powinno dać się do siebie dodać.
#  MyFraction(5, 4) == MyFraction(2, 4) + MyFraction(3, 4)
#Ułamki powinno dać się do siebie porównać.
#        MyFraction(6, 3) == MyFraction(6, 3)
#Dodawanie int też powinno być możliwe.
#  MyFraction(5, 4) == MyFraction(1, 4) + 1
#  MyFraction(5, 4) == 1 + MyFraction(1, 4)


#Instancje klasy MyFraction powinno dać się rzutować na string
#Przykład:
#  'MyFraction(numerator=1, denominator=2)' == str(MyFraction(1, 2))
#  'MyFraction(numerator=1, denominator=2)' == repr(MyFraction(1, 2))
def skracanie(x,y):
  z=min(x,y)
  t=max(x,y)
  while 1:
    if 0 in (z,t):
      if z:
        return int(x/z),int(y/z)
      return int(x/t),int(y/t)
    if z>t:
      z=z-t
    elif t>z:
      t=t-z
    elif t==z:
      return int(x/z),int(y/z)

class MyFraction:
  
  def __init__(self,numerator,denominator=1):
    self.numerator,self.denominator=skracanie(numerator,denominator)
  
  def __add__(self, przekaz):
    if type(przekaz)==int:
      return MyFraction(przekaz*self.denominator+self.numerator,self.denominator)
    return MyFraction(przekaz.denominator*self.numerator+przekaz.numerator*self.denominator,przekaz.denominator*self.denominator)
  
  def __iadd__(self,przekaz):
    if type(przekaz)==int:
      self.numerator=przekaz*self.denominator+self.numerator
      return self
    self.numerator,self.denominator=skracanie(przekaz.denominator*self.numerator+przekaz.numerator*self.denominator,przekaz.denominator*self.denominator)
    return self
  
  def __radd__(self,przekaz):
    return MyFraction(przekaz*self.denominator+self.numerator,self.denominator)
    
  def __str__(self):
    return "MyFraction(numerator="+str(self.numerator)+", denominator="+str(self.denominator)+")"
    
  def __repr__(self):
    return "MyFraction(numerator="+str(self.numerator)+", denominator="+str(self.denominator)+")"
    
  def __eq__(self, przekaz):
    return self.numerator==przekaz.numerator and self.denominator==przekaz.denominator
