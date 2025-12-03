while True:
    fatorial = int(input("Digite um número para calcular o fatorial: "))
    if fatorial >=0:
        print(f'Número válido!')
        break
    else:
        print(f'Número inválido! Tente novamente.')

def calculo(fatorial):
    if fatorial == 0 or fatorial == 1 :
        return 1 
    return fatorial * calculo(fatorial - 1)
print(calculo(fatorial))