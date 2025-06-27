# Função para calcular o fatorial
def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

# Programa principal
n = int(input("Digite um número inteiro positivo: "))

print("\nTabela de fatoriais:")
for i in range(1, n + 1):
    print(f"{i}! = {fatorial(i)}")
