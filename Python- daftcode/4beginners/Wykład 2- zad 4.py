#Zadanie 4
#Napisz funkcję fibonacci_list, która dla zadanego n obliczy n liczb ciągu Fibonacciego, zwracając listę liczb z zadanego ciągu.
def fibonacci_list(n):
  if n==0:
    fib=[]
  if n==1:
    fib=[1]
  elif n==2:
    fib= [1, 1]
  elif n>2:
    fib=[1,1]
    temp=[0]
    for i in range(2,n,1):
        temp[0]=fib[i-2]+fib[i-1]
        fib[len(fib):] =temp
  return fib
    
  
assert fibonacci_list(7) == [1, 1, 2, 3, 5, 8, 13]