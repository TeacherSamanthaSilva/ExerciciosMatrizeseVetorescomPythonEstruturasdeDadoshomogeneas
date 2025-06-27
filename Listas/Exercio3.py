# 1. Lê o grau do polinômio
n = int(input("Digite o grau do polinômio: "))

# 2. Lê os coeficientes e armazena no vetor
coeficientes = []
print("Digite os coeficientes do polinômio (a0 até a" + str(n) + "):")
for i in range(n + 1):
    coef = float(input(f"a[{i}] = "))
    coeficientes.append(coef)

# 3. Lê o valor de x
x = float(input("Digite o valor de x: "))

# 4. Calcula o valor do polinômio em x
p_x = 0
for i in range(n + 1):
    p_x += coeficientes[i] * (x ** i)

# 5. Exibe o resultado
print(f"O valor de p({x}) é: {p_x}")
