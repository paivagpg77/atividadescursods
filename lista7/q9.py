qntdisciplinas = int(input('Quantas disciplinas você quer analisar?: '))
nomes_disciplinas = []
mediasdisciplinas = []
somageral = 0
for d in range(qntdisciplinas):
    nome_disciplina = input(f'\nNome da disciplina {d+1}: ')
    nomes_disciplinas.append(nome_disciplina)
    qntalunos = int(input(f'Quantos alunos há em {nome_disciplina}?: '))
    soma_notas = 0
    for a in range(qntalunos):
        nota = float(input(f'Nota do aluno {a+1} em {nome_disciplina}: '))
        soma_notas += nota
    mediadisciplina = soma_notas / qntalunos
    mediasdisciplinas.append(mediadisciplina)
    somageral += mediadisciplina
media_global = somageral / qntdisciplinas
maiormedia = mediasdisciplinas[0]
menormedia = mediasdisciplinas[0]
discmaior = nomes_disciplinas[0]
discmenor = nomes_disciplinas[0]
for i in range(qntdisciplinas):
    if mediasdisciplinas[i] > maior_media:
        maior_media = mediasdisciplinas[i]
        disc_maior = nomes_disciplinas[i]
    elif mediasdisciplinas[i] < menor_media:
        menor_media = mediasdisciplinas[i]
        disc_menor = nomes_disciplinas[i]
print('\n--- Resultado das análises ---')
for i in range(qntdisciplinas):
    print(f'{nomes_disciplinas[i]} → média da turma: {mediasdisciplinas[i]:.1f}')
print(f'\nMédia global das disciplinas: {media_global:.1f}')
print(f'Disciplina com maior média: {discmaior} ({maiormedia:.1f})')
print(f'Disciplina com menor média: {discmenor} ({menormedia:.1f})')