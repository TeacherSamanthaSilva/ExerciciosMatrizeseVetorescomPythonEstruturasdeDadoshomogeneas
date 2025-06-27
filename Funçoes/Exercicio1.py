def mostrar_maior(valor1, valor2):
    if valor1 > valor2:
        print("O maior valor é:", valor1)
    elif valor2 > valor1:
        print("O maior valor é:", valor2)
    else:
        print("Os dois valores são iguais:", valor1)

# Testando a função
mostrar_maior(10, 20)
mostrar_maior(50, 30)
mostrar_maior(7, 7)
