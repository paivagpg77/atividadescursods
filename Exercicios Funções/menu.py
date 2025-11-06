import math
import random

def data():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))
    print(f"{dia:02d}/{mes:02d}/{ano}")

def calcular_area_circunferencia():
    raio = float(input("Digite o raio da circunferência: "))
    area = math.pi * raio**2
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
        print(f'A palavra 1 que é {palavra1} está contida em {palavra2}')
    else:
        print('A palavra 1 não está contida na palavra 2')

def vetor_aleatorio():
    tamanho = int(input('Digite o tamanho do vetor: '))
    intervalo = int(input('Digite o intervalo mínimo entre os vetores: '))
    fim = int(input('Digite o valor máximo do vetor:  '))
    vetor = [random.randint(intervalo, fim) for _ in range(tamanho)]
    print('O VETOR GERADO ALEATORIAMENTE É ESSE EM BAIXO:')
    print(vetor)
    return vetor

def vetor_maior():
    vetor = vetor_aleatorio()
    maior = max(vetor)
    print(f'O maior vetor é {maior}')

def media_vetor():
    vetor = vetor_aleatorio()
    if len(vetor) == 0:
        print('Não é possível calcular a média do vetor, vetor é vazio')
        return
    media = sum(vetor) / len(vetor)
    print(f'A média dos vetores é igual a {media:.1f}')

def vetor_crescente():
    vetor = vetor_aleatorio()
    vetor_ordenado = sorted(vetor)
    print('O vetor em ordem crescente é:')
    print(vetor_ordenado)

def vetor_decrescente():
    vetor = vetor_aleatorio()
    vetor_ordenado = sorted(vetor, reverse=True)
    print('O VETOR EM ORDEM DECRESCENTE É:')
    print(vetor_ordenado)

def vetor_repetido():
    vetor = vetor_aleatorio()
    vetor_unico = list(dict.fromkeys(vetor))

    if len(vetor) == len(vetor_unico):
        print('Não tem números repetidos.')
    else:
        print('Tinha números repetidos e foram removidos.')

    print('VETOR FINAL (SEM REPETIDOS): ')
    print(vetor_unico)

def matriz_aleatoria():
    linhas = int(input('Digite o número de linhas: '))
    colunas = int(input('Digite o número de colunas: '))
    inferior = int(input('Digite o limite inferior dos valores: '))
    superior = int(input('Digite o limite superior dos valores: '))
    if inferior > superior:
        print('Erro: o limite inferior não pode ser maior que o superior!')
        return
    matriz = [
        [random.randint(inferior, superior) for _ in range(colunas)]
        for _ in range(linhas)
    ]
    print('\nMatriz gerada aleatoriamente:')
    for linha in matriz:
        print(linha)
    return matriz

def media_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    inferior = int(input('Digite o limite inferior dos valores: '))
    superior = int(input('Digite o limite superior dos valores: '))
    if inferior > superior:
        print('Erro: o limite inferior não pode ser maior que o superior!')
        return
    matriz = [
        [random.randint(inferior, superior) for _ in range(colunas)]
        for _ in range(linhas)
    ]
    print('\nMatriz gerada:')
    for linha in matriz:
        print(linha)
    soma = sum(sum(linha) for linha in matriz)
    total = linhas * colunas
    media = soma / total

    print(f'\nA média dos valores da matriz é: {media:.2f}')


def maior_valor_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    inferior = int(input('Digite o limite inferior dos valores: '))
    superior = int(input('Digite o limite superior dos valores: '))

    if inferior > superior:
        print('Erro: o limite inferior não pode ser maior que o superior!')
        return
    matriz = [
        [random.randint(inferior, superior) for _ in range(colunas)]
        for _ in range(linhas)
    ]
    print('\nMatriz gerada:')
    for linha in matriz:
        print(linha)
    maior = max(max(linha) for linha in matriz)
    print(f'\nO maior valor encontrado na matriz é: {maior}')

def matriz_acimabaixo():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    inferior = int(input('Digite o limite inferior dos valores: '))
    superior = int(input('Digite o limite superior dos valores: '))

    if inferior > superior:
        print('Erro: o limite inferior não pode ser maior que o superior!')
        return

    matriz = [[random.randint(inferior, superior) for _ in range(colunas)] for _ in range(linhas)]
    print('\nMatriz gerada:')
    for linha in matriz:
        print(linha)
    todos_valores = [valor for linha in matriz for valor in linha]
    media = sum(todos_valores) / len(todos_valores)

    acima = [v for v in todos_valores if v > media]
    abaixo = [v for v in todos_valores if v < media]

    print(f'\nMédia dos valores: {media:.2f}')
    print(f'Valores acima da média: {acima}')
    print(f'Valores abaixo da média: {abaixo}')

def diagonais_matriz():
    n = int(input('Digite o tamanho da matriz quadrada (ex: 3 para 3x3): '))
    inferior = int(input('Digite o limite inferior dos valores: '))
    superior = int(input('Digite o limite superior dos valores: '))

    if inferior > superior:
        print('Erro: o limite inferior não pode ser maior que o superior!')
        return
    matriz = [[random.randint(inferior, superior) for _ in range(n)] for _ in range(n)]
    print('\nMatriz gerada:')
    for linha in matriz:
        print(linha)
    diag_principal = [matriz[i][i] for i in range(n)]
    diag_secundaria = [matriz[i][n - 1 - i] for i in range(n)]
    print(f'\nDiagonal principal: {diag_principal}')
    print(f'Diagonal secundária: {diag_secundaria}')


print('MENU')
print('[0] SAIR\n[1] FORMAR DATA\n[2] CALCULAR CIRCUNFERÊNCIA\n[3] CONVERSÃO DE TEMPERATURA\n[4] HIPOTENUSA\n[5] EQUAÇÃO SEGUNDO GRAU\n[6] CONTAGEM DE LETRAS\n[7] VER SE PALAVRA ESTÁ CONTIDA NA OUTRA\n[8] GERAR VETOR ALEATÓRIO\n[9] MAIOR VETOR\n[10] MÉDIA DOS VETORES\n[11] ORDENAR VETOR CRESCENTE\n[12] ORDENAR VETOR DECRESCENTE\n[13] REMOVER REPETIDOS')

while True:
    escolha = int(input('Escolha uma tarefa para o executar menu: '))
    if escolha < 0 or escolha > 18:
        print('Número inválido.')
        continue
    if escolha == 0:
        print('Saindo...')
        break
    elif escolha == 1:
        data()
    elif escolha == 2:
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
    elif escolha == 8:
        vetor_aleatorio()
    elif escolha == 9:
        vetor_maior()
    elif escolha == 10:
        media_vetor()
    elif escolha == 11:
        vetor_crescente()
    elif escolha == 12:
        vetor_decrescente()
    elif escolha == 13:
        vetor_repetido()
    elif  escolha == 14:
        matriz_aleatoria()
    elif escolha ==15:
        media_matriz()
    elif escolha ==16:
        maior_valor_matriz()
    elif escolha == 17:
        matriz_acimabaixo()
    elif escolha == 18:
        diagonais_matriz()