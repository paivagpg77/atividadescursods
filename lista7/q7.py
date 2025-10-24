qntalunos = int(input('Quantos alunos você quer analisar: '))
qntaavali = int(input('Quantos avaliações o aluno fez?:'))
medias =  []
nmAlunos = []
soma  = 0 
for a in range(qntalunos):
  nome = input(f'Qual o nome do {a+1}: ')
  nmAlunos.append(nome)
  soman = 0 
  for g in range(qntaavali):
    nota = float(input(f'Qual a nota do aluno/a {v+1} do aluno {nome}?: '))
    somant += nota 
  mediaaln = somant / qntaavali
  medias.append(mediaaln)
  smturma +=  mediaaln
mediatrm = smturma  / qntalunos
maiormedia = medias[0]
menormedia  = medias[0]
alunomaior =  nmAlunos[0]
alunomenor = nmAlunos[0]
for i in range(qntalunos):
  if medias[i] > maiormedia:
    maiormedia = medias[i]
    alunomaior  = nmAlunos[i]
  elif medias[i] < menormedia:
    menormedia  = medias[i]
    alunomenor  = nmAlunos[i]
print('---Resultados dos alunos---')
for i in range(qntalunos):
  print(f'{nmAlunos} : média = {medias[i]:.1f}')
print(f'Média geral da turma foi {mediatrm:.1f}')
print(f'A maior média foi {maiormedia:.1f}')
print(f'A menor média foi {menormedia:.1f}')