# Função que concatena as colunas de duas matrizes
def concatenar_matrizes(A, B):
    # Verifica se o número de linhas é igual
    if len(A) != len(B):
        return "Erro: As matrizes devem ter o mesmo número de linhas."
    
    # Concatena as colunas
    matriz_resultante = []
    for i in range(len(A)):
        linha_concatenada = A[i] + B[i]
        matriz_resultante.append(linha_concatenada)

    return matriz_resultante

# Programa principal para testar a função
def main():
    A = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    resultado = concatenar_matrizes(A, B)

    print("Matriz concatenada:")
    for linha in resultado:
        print(linha)

# Executa o programa
main()
