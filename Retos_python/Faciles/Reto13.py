import math

def atri(altura, base):
      area = (altura * base) / 2
      return area
  
  
def acir(radio):
    area = math.pi * radio**2
   
    return area

def reto13(a, b, r):
  print(f'Triangulo: {atri(a, b)}')
  print(f'Circulo: {acir(r)}')

reto13(1,3,5)