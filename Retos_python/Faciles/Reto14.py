from Retos.Faciles.Reto13 import acir



def vcil(radio, longitud):
  
  area =  acir(radio)* longitud

  return area
  
def reto14(r,l):
  print(f'Volumen Cilindro: {vcil(r,l)}')

reto14(1,2)