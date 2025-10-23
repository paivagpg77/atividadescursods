
numVendedores = int(input("Digite o número de vendedores: "))
vendedores = []
venda_por_vendedor = []
for j in range(numVendedores):
    nomeVendedor = input(f"\nDigite o nome do vendedor {j+1}: ")
    vendedores.append(nomeVendedor)
    numVendas = int(input(f"Digite o número de vendas do(a) {nomeVendedor}: "))
    totalVendedor = 0
    for i in range(numVendas):
        valorVenda = float(input(f"Digite o valor da {i+1}ª venda: R$ "))
        totalVendedor += valorVenda
    venda_por_vendedor.append(totalVendedor)
print("\n--- TOTAL DE VENDAS POR VENDEDOR ---")
for i in range(numVendedores):
    print(f"{vendedores[i]} vendeu um total de R$ {venda_por_vendedor[i]:.2f}")
somaVendas = 0
maior = venda_por_vendedor[0]
menor = venda_por_vendedor[0]
vendedorMaior = vendedores[0]
vendedorMenor = vendedores[0]
for i in range(numVendedores):
    somaVendas += venda_por_vendedor[i]
    if venda_por_vendedor[i] > maior:
        maior = venda_por_vendedor[i]
        vendedorMaior = vendedores[i]
    if venda_por_vendedor[i] < menor:
        menor = venda_por_vendedor[i]
        vendedorMenor = vendedores[i]
mediaTotal = somaVendas / numVendedores
print("\n--- RESULTADOS FINAIS ---")
print(f"Média de vendas da equipe: R$ {mediaTotal:.2f}")
print(f"Vendedor que mais vendeu: {vendedorMaior} com R$ {maior:.2f}")
print(f"Vendedor que menos vendeu: {vendedorMenor} com R$ {menor:.2f}")
