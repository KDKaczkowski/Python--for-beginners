'''Dla modelowej lub swojej klasy MyFraction dodaj walidację wejścia i przetwarzania.
Tym razem oczekujemy że MyFraction będzie obsługiwać nie tylko dodawanie ale również:
    odejmowanie
    mnożenie
    dzielenie

MyFraction ma nie działać z "podwójnymi" operatorami np ** // i rzucać odpowiednim wyjątkiem
Jak i przekazywanie ułamków jako licznik czy mianownik.
Przykład:
    MyFraction(1, 2) * MyFraction(1, 2) == MyFraction(1, 4)
    MyFraction(numerator=1, denominator=MyFraction(1,2)) == MyFraction(2, 1)
    MyFraction(2, 3) / MyFraction(1, 3) == MyFraction(2, 1)


Klasa MyFraction powinna też móc się dodawać, odejmować, mnożyć i dzielić
    z liczbami zmiennoprzecinkowymi ale:
    nie musi ich przyjmować jako argumenty
    wynik operacji z operandem typu float jest typu float
    MyFraction można przedstawić w notacji zmiennoprzecinkowej
Przykład:
    0.5 + MyFraction(1, 2) == 1.0
    float(MyFraction(3, 20)) == 0.15

Dodatkowo wejście może nie być poprawne.
Z tego powodu klasa MyFraction powinna walidować wejściowe parametry i ich poprawność.

By to osiągnąć zaimplementuj następujące wyjątki dziedziczące po wbudowanych wyjątkach:
    InvalidOperandError
    InvalidInputOperandError
    OperationNotSupportedError

Przykład:
    MyFraction(5, 4) + "10"   #  <- ten test ma rzucić wyjątkiem InvalidOperand
    MyFraction(5, [12])       #  <- ten test ma rzucić wyjątkiem InvalidInputOperand
    MyFraction(99, 100)**2    #  <- ten test ma rzucić wyjątkiem OperationNotSupported

Klasa MyFraction nie musi obsługiwać liczb ujemnych - w testach nigdy nie dojdzie do sytuacji gdzie wynik operacji matematycznej jest ujemny.

Pamiętaj jednak że wszystkie dotychczasowej operacje na MyFraction z Zadania 3.1 powinny
wciąż działać.

UWAGA: Testy porównujące ze sobą floaty są wykonywane z domyślną dokładnością funkcji assertAlmostEqual z frameworku unittest tj z dokładnością do 7mego miejsca po przecinku
'''

import math

class InvalidOperandError(Exception):
  pass
class InvalidInputOperandError(Exception):
  pass
class OperationNotSupportedError(Exception):
  pass

class MyFraction:
  
  def __init__(self, numerator, denominator=1):
    if (type(numerator)==MyFraction and type(denominator)==int):
      self.numerator = numerator.numerator
      self.denominator = numerator.denominator*denominator
      
    elif (type(numerator)==int and type(denominator)==int):
      self.numerator = numerator
      self.denominator = denominator
      
    elif (type(numerator)==int and type(denominator)==MyFraction):
      self.numerator=numerator*denominator.denominator
      self.denominator=denominator.numerator
      
    elif (type(numerator)==MyFraction and type(denominator)==MyFraction):
      self.numerator=numerator.numerator*denominator.denominator
      self.denominator=numerator.denominator*denominator.numerator
      
    else:
      raise InvalidInputOperandError()
    self._reduce()

  def _reduce(self):
    nd_gcd = math.gcd(
      self.numerator, self.denominator
    )
    self.numerator //= nd_gcd
    self.denominator //= nd_gcd
    
  def __add__(self, przekaz):
    if type(przekaz)==float:
      return  przekaz+self.numerator/self.denominator
      
    elif type(przekaz)==int:
      return MyFraction(przekaz*self.denominator+self.numerator,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(przekaz.denominator*self.numerator+przekaz.numerator*self.denominator,przekaz.denominator*self.denominator)
      
    else:
      raise InvalidOperandError()
      
  def __iadd__(self,przekaz):
    if (type(przekaz)==float):
      return przekaz+self.numerator/self.denominator
      
    elif (type(przekaz)==int):
      self.numerator=przekaz*self.denominator+self.numerator
      return self
      
    elif (type(przekaz)==MyFraction):
      self.numerator,self.denominator=przekaz.denominator*self.numerator+przekaz.numerator*self.denominator,przekaz.denominator*self.denominator
      self._reduce()
      return self
      
    else:
      raise InvalidOperandError()
    
  
  def __radd__(self,przekaz):
    if type(przekaz)==float:
      return przekaz+(self.numerator/self.denominator)
      
    elif type(przekaz)==int:
      return MyFraction(przekaz*self.denominator+self.numerator,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(przekaz*self.denominator+self.numerator,self.denominator)
      
    else:
      raise InvalidOperandError()
    
  def __str__(self):
    return "MyFraction(numerator="+str(self.numerator)+", denominator="+str(self.denominator)+")"
    
  def __repr__(self):
    return "MyFraction(numerator="+str(self.numerator)+", denominator="+str(self.denominator)+")"
    
  def __eq__(self, przekaz):
    return self.numerator==przekaz.numerator and self.denominator==przekaz.denominator
  
  def __sub__(self,przekaz):
    if type(przekaz)==float:
      return self.numerator/self.denominator-przekaz
      
    elif type(przekaz)==int:
      return MyFraction(self.numerator - przekaz*self.denominator,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(self.numerator*przekaz.denominator - (przekaz.numerator*self.denominator),self.denominator*przekaz.denominator)
      
    else:
      raise InvalidOperandError()
  
  def __rsub__(self,przekaz):
    if type(przekaz)==float:
      return przekaz-self.numerator/self.denominator
      
    elif type(przekaz)==int:
      return MyFraction(przekaz*self.denominator - self.numerator,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction( (przekaz.numerator*self.denominator)- self.numerator*przekaz.denominator,self.denominator*przekaz.denominator)
      
    else:
      raise InvalidOperandError()

  def __mul__(self,przekaz):
    if type(przekaz)==float:
      return self.numerator/self.denominator*przekaz
      
    elif type(przekaz)==int:
      return MyFraction(self.numerator*przekaz,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(self.numerator*przekaz.numerator,self.denominator*przekaz.denominator)
      
    else:
      raise InvalidOperandError()
  
  def __rmul__(self,przekaz):
    if type(przekaz)==float:
      return przekaz*self.numerator/self.denominator
      
    elif type(przekaz)==int:
      return MyFraction(przekaz*self.numerator,self.denominator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(przekaz.numerator*self.numerator,przekaz.denominator*self.denominator)
      
    else:
      raise InvalidOperandError()
  
  def __truediv__(self,przekaz):
    
    if type(przekaz)==float:
      if przekaz==0.0:
        raise InvalidInputOperandError
      return self.numerator/(self.denominator*przekaz)
      
    elif type(przekaz)==int:
      if przekaz==0:
        raise InvalidInputOperandError
      return MyFraction(self.numerator,self.denominator*przekaz)
      
    elif type(przekaz)==MyFraction:
      if przekaz.numerator==0:
        raise InvalidInputOperandError()
      return MyFraction(self.numerator*przekaz.denominator,self.denominator*przekaz.numerator)
      
    else:
      raise InvalidOperandError()

  def __rtruediv__(self,przekaz):
    if self.numerator==0:
      raise InvalidOperandError()
    elif type(przekaz)==float:
      return (przekaz*self.denominator)/self.numerator
      
    elif type(przekaz)==int:
      return MyFraction(przekaz*self.denominator,self.numerator)
      
    elif type(przekaz)==MyFraction:
      return MyFraction(self.denominator*przekaz.numerator,self.numerator*przekaz.denominator)
      
    else:
      raise InvalidOperandError()

  def __isub__(self,przekaz):
    if (type(przekaz)==float):
      return self.numerator/self.denominator - przekaz
      
    elif (type(przekaz)==int):
      self.numerator=self.numerator - przekaz*self.denominator
      return self
      
    elif (type(przekaz)==MyFraction):
      self.numerator,self.denominator=przekaz.denominator*self.numerator-przekaz.numerator*self.denominator,przekaz.denominator*self.denominator
      self._reduce()
      return self
      
    else:
      raise InvalidOperandError()
  
  def __imul__(self,przekaz):
    if (type(przekaz)==float):
      return self.numerator/self.denominator*przekaz
      
    elif (type(przekaz)==int):
      self.numerator=self.numerator*przekaz
      self._reduce()
      return self
      
    elif (type(przekaz)==MyFraction):
      self.numerator,self.denominator=przekaz.numerator*self.numerator,przekaz.denominator*self.denominator
      self._reduce()
      return self
      
    else:
      raise InvalidOperandError()

  def __itruediv__(self,przekaz):
    
    if (type(przekaz)==float):
      if przekaz==0.0:
        raise InvalidInputOperandError()
      return self.numerator/self.denominator/przekaz
      
    elif (type(przekaz)==int):
      if przekaz==0:
        raise InvalidInputOperandError()
      self.denominator=self.denominator*przekaz
      self._reduce()
      return self
      
    elif (type(przekaz)==MyFraction):
      if przekaz.numerator==0:
        raise InvalidInputOperandError()
      self.numerator,self.denominator=self.numerator*przekaz.denominator,self.denominator*przekaz.numerator
      self._reduce()
      return self
      
    else:
      raise InvalidOperandError()
  
  def __pow__(self,przekaz):
    raise OperationNotSupportedError()
  def __floordiv__(self,przekaz):
    raise OperationNotSupportedError()
  def __lshift__(self, inny):
    raise OperationNotSupportedError()
  def __rshift__(self, inny):
    raise OperationNotSupportedError()