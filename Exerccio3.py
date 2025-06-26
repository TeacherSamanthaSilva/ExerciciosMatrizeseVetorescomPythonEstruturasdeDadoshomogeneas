def main():
    # Inicializa a matriz 3x2
    matriz = []
    
    print("Digite os valores da matriz 3x2:")
    for i in range(3):
        linha = []
        for j in range(2):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    # Calcula SOMALINHA
    SOMALINHA = []
    for linha in matriz:
        soma = sum(linha)
        SOMALINHA.append(soma)

    # Calcula TOTAL
    TOTAL = sum(SOMALINHA)

    # Exibe a matriz
    print("\nMatriz:")
    for linha in matriz:
        print(linha)

    # Exibe o vetor SOMALINHA
    print("\nSoma de cada linha (SOMALINHA):", SOMALINHA)

    # Exibe o TOTAL
    print("\nTOTAL das somas das linhas:", TOTAL)

# Executa o programa
main()
