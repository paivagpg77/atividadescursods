print('Olá professor, digite os dados dos alunos para calcular a média.')
alunos_detalhes = []
quantidade_alunos = int(input("Quantos alunos você quer calcular a média? "))
for i in range(quantidade_alunos):
    nome = input(f"\nDigite o nome do aluno {i+1}: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    media = (nota1 + nota2) / 2
    aluno_info = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media
    }
    alunos_detalhes.append(aluno_info)
print("\nResumo das notas dos alunos:")
for aluno in alunos_detalhes:
    print(f"{aluno['nome']}: Nota 1 = {aluno['nota1']}, Nota 2 = {aluno['nota2']}, Média = {aluno['media']:.2f}")