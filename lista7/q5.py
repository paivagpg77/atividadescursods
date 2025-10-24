numAtletas = int(input('Quantos atletas executaram a atividade?: '))
numetletas = []
numdistancia = []
soma = 0
for t in range(numAtletas):
  nome = input(f'Nome do atleta {t+1}?:')
  distancia = float(input(f'O Atleta {nome} percorreu quantos metros?: '))
  numetletas.append(nome)
  numdistancia.append(distancia)
  soma += distancia
media = soma/numAtletas
print('---Resultado das média---')
for i in range(numAtletas):
  print(f'{numetletas[i]} percorreu a distancia de {numdistancia[i]}')
print(f'As médias de distância dos atletas foram {media:.1f}')
maior = 0
menor = 0
distamenor = numdistancia[0]
distamaior = numdistancia[0]
soma = 0 
for a in range(numAtletas):
  soma += numdistancia
  if numdistancia[a] > maior:
    maior = numdistancia
    distamaior = numetletas
  elif numdistancia[a] < menor:
    menor = numdistancia[a]
    distamenor = numdistancia[a]
print(f'O que alcançou a maior distância foi{distamaior}')
print(f'O que alcançou a menor distância foi{distamenor}')