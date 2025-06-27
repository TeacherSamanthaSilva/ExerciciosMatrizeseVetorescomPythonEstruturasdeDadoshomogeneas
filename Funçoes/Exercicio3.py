# Função que retorna o menor entre três números
def menor_valor(a, b, c):
    return min(a, b, c)  # min() retorna o menor valor

# Testando a função com diferentes valores
print("O menor valor é:", menor_valor(2, 4, 9))   # Deve mostrar 2
print("O menor valor é:", menor_valor(10, 5, 8))  # Deve mostrar 5
print("O menor valor é:", menor_valor(7, 7, 3))   # Deve mostrar 3
