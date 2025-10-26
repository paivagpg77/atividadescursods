qntalunos = int(input('Quantos alunos você quer analisar: '))
qntaavali = int(input('Quantas avaliações cada aluno fez?: '))
medias = []
nmAlunos = []
smturma = 0
for a in range(qntalunos):
    nome = input(f'\nNome do aluno {a+1}: ')
    nmAlunos.append(nome)
    somant = 0
    for g in range(qntaavali):
        nota = float(input(f'Nota {g+1} de {nome}: '))
        somant += nota
    mediaaln = somant / qntaavali
    medias.append(mediaaln)
    smturma += mediaaln
mediatrm = smturma / qntalunos
maiormedia = medias[0]
menormedia = medias[0]
alunomaior = nmAlunos[0]
alunomenor = nmAlunos[0]
for i in range(qntalunos):
    if medias[i] > maiormedia:
        maiormedia = medias[i]
        alunomaior = nmAlunos[i]
    elif medias[i] < menormedia:
        menormedia = medias[i]
        alunomenor = nmAlunos[i]
print('\n--- Resultados dos alunos ---')
for i in range(qntalunos):
    print(f'{nmAlunos[i]}: média = {medias[i]:.1f}')
print(f'\nMédia geral da turma: {mediatrm:.1f}')
print(f'Maior média: {maiormedia:.1f} ({alunomaior})')
print(f'Menor média: {menormedia:.1f} ({alunomenor})')
