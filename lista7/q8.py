qntcaminhao = int(input('Quantos caminhões você quer analisar?: '))
numcaminhao = []
pesos = []
soma = 0
for i in range(qntcaminhao): 
    nucaminhao = input(f'Qual o nome do caminhão {i+1}: ')
    peso = float(input(f'Qual a quantidade de peso que o {nucaminhao} carregou?: '))
    numcaminhao.append(nucaminhao)
    pesos.append(peso)
    soma += peso
media = soma / qntcaminhao
pesomaior = pesos[0]
pesomenor = pesos[0]
caminhaomaior = numcaminhao[0]
caminhaomenor = numcaminhao[0]
for i in range(qntcaminhao):
    if pesos[i] > pesomaior:
        pesomaior = pesos[i]
        caminhao_maior = numcaminhao[i]
    elif pesos[i] < pesomenor:
        pesomenor = pesos[i]
        caminhao_menor = numcaminhao[i]
print('\n--- Resultado das análises ---')
for i in range(qntcaminhao):
    print(f'O caminhão {numcaminhao[i]} carregou {pesos[i]:.1f} kg')
print(f'\nA média de peso dos caminhões foi {media:.1f} kg')
print(f'O caminhão que carregou o MAIOR peso foi {caminhaomaior}, com {pesomaior:.1f} kg')
print(f'O caminhão que carregou o MENOR peso foi {caminhaomenor}, com {pesomenor:.1f} kg')