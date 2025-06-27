# 1. Lê o tamanho dos vetores
n = int(input("Digite o número de elementos dos vetores: "))

# 2. Lê os valores do vetor x
x = []
print("Digite os valores do vetor x:")
for i in range(n):
    valor = int(input(f"x[{i}]: "))
    x.append(valor)

# 3. Lê os valores do vetor y
y = []
print("Digite os valores do vetor y:")
for i in range(n):
    valor = int(input(f"y[{i}]: "))
    y.append(valor)

# 4. Calcula o produto escalar
produto_escalar = 0
for i in range(n):
    produto_escalar += x[i] * y[i]

# 5. Exibe o resultado
print("Produto escalar =", produto_escalar)
