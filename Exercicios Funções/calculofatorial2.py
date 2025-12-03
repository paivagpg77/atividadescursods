num = int(input('Digite um número para calcular o fatorial:'))
def fatorial(num):
    if num == 1  or num == 0 :
        return 1
    return num * fatorial(num-1)
print(fatorial(num))