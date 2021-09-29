'''
Returneaza true daca n este prim si false daca nu.
'''
from math import sqrt

def is_prime(n):
  if n == 1 or n ==0:
    return False
  if n == 2:
    return True
  if n == 3:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True
  
  '''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  prod = 1
  for number in lst:
    prod*=number
  return prod


  
  
  '''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if x == 0:
    return y
  elif y == 0:
    return x
  while(x != y):
    if(x > y):
      x-=y
    else:
      y-=x
  return x

  
  
  '''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while(x != 0):
    aux = x
    x = x % y
    y = aux
  return y

def main():
  print('''
  1.IS prime
  2. Product
  3. Cmmdc v1
  4. Cmmdc v2''')
  x = int(input("Comanda="))
  if(x == 1):
    n=int(input("Introduceti n="))
    print(is_prime(n))

  if (x == 2):
    n = int(input("Introduceti n="))
    list = []
    for i in range(0,n):
      element = int(input())
      list.append(element)
    print(get_product(list))

  if (x == 3):
    n = int(input("Introduceti n="))
    m = int(input("Introduceti m="))
    print(get_cmmdc_v1(n, m))

  if (x == 4):
    n = int(input("Introduceti n="))
    m = int(input("Introduceti m="))
    print(get_cmmdc_v2(n, m))

  if x not in [1,2,3,4]:
    print("No identifiable option, bye.")

if __name__ == '__main__':
  main()
