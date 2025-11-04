import math
def hipotenusa():
  cateto1 = float(input('Diga o valor do primeiro cateto: '))
  cateto2 = float(input('Diga o valor do segundo cateto: '))
  resultado1 = cateto1**2 + cateto2**2 
  hipotenusa = math.sqrt(resultado1)
  print(f'O valor da hipotenusa é {hipotenusa:.1f}')
hipotenusa()