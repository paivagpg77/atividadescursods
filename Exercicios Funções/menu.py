import math
import random
def data():
  dia = int(input('Digite o dia: '))
  mes = int(input('Digite o mês: '))
  ano = int(input('Digite o ano: '))
  print(f"{dia:02d}/{mes:02d}/{ano}")

def calcular_area_circunferencia(raio):
    return math.pi * raio**2
    raio = float(input("Digite o raio da circunferência: "))
    area = calcular_area_circunferencia(raio)
    print("A área da circunferência é:", area)

def conversao():
  fahr = int(input("Diga a temperatura em Fahrenheit: "))
  celsius = (fahr - 32) * (5/9)
  print(f'A conversão de temperatura é {celsius:.1f}')

def hipotenusa():
  cateto1 = float(input('Diga o valor do primeiro cateto: '))
  cateto2 = float(input('Diga o valor do segundo cateto: '))
  resultado1 = cateto1**2 + cateto2**2 
  hipotenusa = math.sqrt(resultado1)
  print(f'O valor da hipotenusa é {hipotenusa:.1f}')


def equacao():
    a = int(input('Digite o valor A da equação: '))
    b = int(input('Digite o valor B da equação: '))
    c = int(input('Digite o valor C da equação: '))
    print('Sua Equação do segundo grau é ↓')
    print(f"{a}x\u00B2 + {b}x + {c} = 0")
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

def gerar_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int(input("Digite o limite superior: "))

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = random.randint(limite_inferior, limite_superior)
            linha.append(valor)
        matriz.append(linha)

    print("\nMatriz gerada:")
    for linha in matriz:
        print(linha)

print('MENU')
print('[0] SAIR \n [1]FORMANDO DATA \n [2] CALCULANDO CIRCUNFERÊNCIA \n [3] CONVERSÃO DE TEMPERATURA \n [4] HIPOTENUSA \n [5] EQUAÇÃO SEGUNDO GRAU')

while True:
    while True:
      escolha = int(input('Escolha qual o seu item do Menu você quer: '))
      if escolha < 0 or  escolha > 5:

          print('Número invalido..')
      else:
          break
    if escolha == 0:
      print('Saindo...')
      break
    if escolha == 1:
            data()
    elif escolha ==2:
            calcular_area_circunferencia()
    elif escolha == 3:
            conversao()
    elif escolha == 4:
            hipotenusa()
    elif escolha == 5:
            equacao()
