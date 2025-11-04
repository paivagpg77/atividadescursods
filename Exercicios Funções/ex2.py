def conversao():
  fahr = int(input("Diga a temperatura em Fahrenheit: "))
  celsius = (fahr - 32) * (5/9)
  print(f'A conversão de temperatura é {celsius:.1f}')
conversao()

