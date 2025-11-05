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

def contagem_letra():
    palavra = input('Digite uma palavra: ')
    contagem = {}
    for letra in palavra:
      if letra in contagem:
        contagem[letra] += 1
      else:
          contagem[letra] = 1 
    print(contagem)
  
def palavra_contida():
    palavra1 = input('Digite a primeira palavra: ').upper()
    palavra2 = input('Digite a segunda palavra: ').upper()
    
    if palavra1 in palavra2:
        print(f'A palavra 1 que é {palavra1} está contido em {palavra2}')
    else:
        print('A palavra 1 não está contida na palavra 2')


def vetor_aleatorio():
  tamanho = int(input('Digite o tamanho do vetor: '))
  intervalo = int(input('Digite o intervalo mínimo entre os vetores: '))
  fim = int(input('Digite o valor máximo do vetor:  '))
  vetor = [random.randint(intervalo, fim) for _ in range(tamanho)]
  print('O VETOR GERADO ALEATORIAMENTE É ESSE EM BAIXO')
  print(vetor)
  return vetor

def vetor_maior():
  vetor = vetor_aleatorio()
  maior = max(vetor)  
  print(f'O maior vetor é {maior}')


print('MENU')
print('[0] SAIR \n [1]FORMANDO DATA \n [2] CALCULANDO CIRCUNFERÊNCIA \n [3] CONVERSÃO DE TEMPERATURA \n [4] HIPOTENUSA \n [5] EQUAÇÃO SEGUNDO GRAU \n [6] CONTAGEM DE LETRAS \n [7] VER SE A PALAVRA ESTÁ CONTIDA NA OUTRA \n [8] GERACÃO DE VETOR ALEATÓRIO \n [9] CALCULANDO MAIOR VETOR'
 )

while True:
    while True:
      escolha = int(input('Escolha qual o seu item do Menu você quer: '))
      if escolha < 0 or  escolha > 9:

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
    elif escolha == 6:
      contagem_letra()
    elif escolha == 7:
      palavra_contida()
    elif escolha ==8:
      vetor_aleatorio()
    elif escolha == 9:
      vetor_maior()