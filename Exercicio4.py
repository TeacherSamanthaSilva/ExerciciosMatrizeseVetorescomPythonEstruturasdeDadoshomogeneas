def main():
    # Matriz de exemplo
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Matriz original:")
    for linha in A:
        print(linha)

    # Chama a função para transpor
    transposta = transpor_matriz(A)

    print("\nMatriz transposta:")
    for linha in transposta:
        print(linha)

# Função que retorna a transposta da matriz
def transpor_matriz(matriz):
    transposta = [list(coluna) for coluna in zip(*matriz)]
    return transposta

# Executa o programa
main()
