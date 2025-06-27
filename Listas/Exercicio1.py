# 1. Solicita o número de elementos
n = int(input("Quantos números você deseja inserir? "))

# 2. Cria o vetor e lê os valores
vetor = []
for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# 3. Imprime os valores na ordem inversa
print("Números na ordem inversa:")
for i in range(n-1, -1, -1):
    print(vetor[i])
