# Função que retorna o maior valor de cada linha
def maiores_por_linha(matriz):
    maiores = []
    for linha in matriz:
        maior = max(linha)
        maiores.append(maior)
    return maiores

# Programa principal para testar a função
def main():
    # Exemplo de matriz
    matriz = [
        [4, 8, 6],
        [1, 5, 9],
        [7, 2, 3]
    ]

    # Chama a função e guarda o resultado
    resultado = maiores_por_linha(matriz)

    # Mostra o vetor com os maiores valores
    print("Maiores valores por linha:", resultado)

# Executa o programa
main()
