qtCidades = int(input('Digite a quantidade de cidades: '))
listaCidades = []
mediasPorCidade = []
somaGeral = 0
totalDias = 0
for j in range(qtCidades):
    nomeCidade = input(f'\nDigite o nome da {j+1}ª cidade: ')
    qtDias = int(input(f'Digite a quantidade de dias de medição em {nomeCidade}: '))
    somaTemp = 0
    for i in range(qtDias):
        tempDia = float(input(f'Digite a temperatura do dia {i+1}: '))
        somaTemp += tempDia
    mediaCidade = somaTemp / qtDias
    listaCidades.append(nomeCidade)
    mediasPorCidade.append(mediaCidade)
    somaGeral += somaTemp
    totalDias += qtDias
mediaGeral = somaGeral / totalDias
maisQuente = mediasPorCidade[0]
maisFria = mediasPorCidade[0]
cidadeMaisQuente = listaCidades[0]
cidadeMaisFria = listaCidades[0]

for i in range(1, qtCidades):
    if mediasPorCidade[i] > maisQuente:
        maisQuente = mediasPorCidade[i]
        cidadeMaisQuente = listaCidades[i]
    if mediasPorCidade[i] < maisFria:
        maisFria = mediasPorCidade[i]
        cidadeMaisFria = listaCidades[i]
print('\n' + '-'*40)
print('RESULTADO FINAL')
print('-'*40)
for i in range(qtCidades):
    print(f'A cidade {listaCidades[i]} teve média de {mediasPorCidade[i]:.2f}°C')
print('-'*40)
print(f'Cidade mais quente: {cidadeMaisQuente} ({maisQuente:.2f}°C)')
print(f'Cidade mais fria: {cidadeMaisFria} ({maisFria:.2f}°C)')
print(f'Temperatura média geral: {mediaGeral:.2f}°C')






