# Solicita ao usuário que insira um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Inicializa uma variável para contar os números ímpares
    contador = 0

    # Inicializa o primeiro número ímpar
    numero_impar = 1

    # Loop para imprimir os n primeiros números ímpares
    while contador < n:
        print(numero_impar)

        # Atualiza o número ímpar e o contador
        numero_impar += 2
        contador += 1
