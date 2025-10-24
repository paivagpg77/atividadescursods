produtos = int(input("Quantos produtos quer avaliar?: "))
soma = 0
nmpdt = []
avaliacoes = []
for p in range(produtos):
    nome = input(f"Nome do produto {p+1}?: ")
    avaliacao = int(input(f"Avalie o {nome} produto (1 a 10): "))
    nmpdt.append(nome)
    avaliacoes.append(avaliacao)
    soma += avaliacao
media = soma/produtos
print(f'\n ---Resultado das média---')
for i in range(produtos):
  print(f'{nmpdt[i]} recebeu avaliação {avaliacoes[i]}')
print(f'\n A média das avaliações é {media:.2f}')
maior = avaliacoes[0]
menor = avaliacoes[0]
pdtmaior =  nmpdt[0]
pdtmenor = nmpdt[0]
soma = 0
for j in range(produtos):
  soma += avaliacoes[j]
  if avaliacoes[j] > maior:
    maior = avaliacoes[j]
    pdtmaior = nmpdt[j]
  elif avaliacoes[j] < menor:
    menor = avaliacoes[j]
    pdtmenor = nmpdt[j]
print(f'O mais bem avaliado foi {pdtmaior}')
print(f'O mais mal avaliado foi {pdtmenor}')
