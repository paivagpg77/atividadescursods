n = int(input("Digite um número para calcular o fatorial: "))

def fatorial(n):
  if n < 0 :
    return 1 
  elif n == 0 or n ==1: 
    return 1 
  else: 
    resultado = 1 
    for i in range(1 ,n+1):
      resultado*=i
    return resultado

print(fatorial(n))