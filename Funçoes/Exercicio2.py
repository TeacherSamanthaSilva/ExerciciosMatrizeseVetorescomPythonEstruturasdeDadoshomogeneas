import math  # para usar o valor de π (pi)

# Função para calcular a área do círculo
def calcular_area(raio):
    return math.pi * raio ** 2

# Função para calcular o perímetro do círculo
def calcular_perimetro(raio):
    return 2 * math.pi * raio

# Programa principal
raio = float(input("Digite o raio do círculo: "))

area = calcular_area(raio)
perimetro = calcular_perimetro(raio)

print(f"A área do círculo é: {area:.2f}")
print(f"O perímetro do círculo é: {perimetro:.2f}")
