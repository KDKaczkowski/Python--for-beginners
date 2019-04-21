# zadanie 4
#Wykład 1 - Zadanie 4
#Napisz program tworzący ze zbioru U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'} zbiór zawierający wszystkie podzbiory U (włącznie z pustym i U).

#UWAGA: w Pythonie zbiory (set) nie mogą być elementami innych zbiorów, proszę użyć frozenset jako zbiorów wewnętrznych.

#Wynik przypisz do zmienej result.

U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'}
LU2=list(U)

result = []
result.append(frozenset(U))
result.append(frozenset())
for n in range(1024):
  binarne=list(bin(n)[2:])
  if n==0:
    continue
  else:
    m=10-len(binarne)
    temp=[]
    for k in range(len(binarne)):
      if int(binarne[k]):
        temp.append(LU2[m+k])
    result.append(frozenset(temp))

assert frozenset(('👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌')) in result