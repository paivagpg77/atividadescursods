qntfiliais = int(input('Quantas filiais você quer analisar?: '))
qntmeses = int(input('Quantos meses você quer analisar?: '))
nmfiliais = []
mediafiliais = []
somageral = 0
for i in range(qntfiliais):
  nomefilial = input(f'Qual o nome da filial {i+1}?: ')
  nmfiliais.append(nomefilial)
  somafaturamento = 0
  for m in range(qntmeses):
    faturamento = float(input(f'Qual o faturamento do mês {m+1} da filial {nomefilial}: R$'))
    somafaturamento += faturamento
  mediadasfiliais = somafaturamento / qntmeses
  mediafiliais.append(mediadasfiliais)
  somageral += mediadasfiliais
mediaTotal = somageral / qntfiliais
maiormedia = mediafiliais[0]
menormedia = mediafiliais[0]
filialmaior = nmfiliais[0]
filialmenor = nmfiliais[0]
for i in range(qntfiliais):
  if mediafiliais[i] > maiormedia:
    maiormedia = mediafiliais[i]
    filialmaior = nmfiliais[i]
  elif mediafiliais[i] < menormedia:
    menormedia = mediafiliais[i]
    filialmenor = nmfiliais[i]
print('---Apuração das análises---')
for i in range(qntfiliais):
  print(f'{nmfiliais[i]} - média dos faturamentos: R${mediafiliais[i]:.3f}')
print(f'\nMédia total de todas as filiais: R${mediaTotal:.2f}')
print(f'A filial com a MAIOR média de faturamento foi {filialmaior}, com R${maiormedia:.3f}')
print(f'A filial com a MENOR média de faturamento foi {filialmenor}, com R${menormedia:.3f}')
