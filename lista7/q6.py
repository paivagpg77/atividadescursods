qntddProdutos= int(input('Quantos produtos você quer vê o lucro?: '))
nmPdt = []
precoCp = []
precoVd = []
lucros = []
soma = 0
for p in range(qntddProdutos):
  nomepdt = input(f'Qual o nome do {p+1} produto?: ')
  compra = float(input(f'Qual o preço de compra do produto {nomepdt}: '))
  venda =  float(input(f'Qual o preço de venda do produto {nomepdt}: '))
  nmPdt.append(nomepdt)
  precoCp.append(compra)
  precoVd.append(venda)
  lucro = venda - compra
  lucros.append(lucro)
soma += lucro
media = soma  / qntddProdutos
print(f'-*-Resultados dos produtos-*-')
for r in range(qntddProdutos):
  print(f'O produto {nmPdt[r]} com o preço R${precoCp[r]}, Teve o lucro de R${lucros[r]:.2f}')
maiorlucro = lucros[0]
menorlucro = lucros[0]
pdtmaior = nmPdt[0]
pdtmenor = nmPdt[0]
for g in range(qntddProdutos):
  if lucros[g] > maiorlucro:
    maiorlucro = lucros[g]
    pdtmaior = nmPdt[g]
  elif lucros[g] < menorlucro:
    menorlucro = lucros[g]
    pdtmenor = nmPdt[g]
print(f'O produto mais lucrativo foi o {pdtmaior} com o lucro de R${maiorlucro:.2f}')
print(f'O produto menor lucrativo foi o {pdtmenor} com o lucro de R${menorlucro:.2f}')
print(f'O lucro médio da loja foi {media:.2f}')