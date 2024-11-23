# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Solicita ao usuário que insira um número natural
n = int(input("Digite um número natural: "))

# Verifica se o número é não-negativo
if n < 0:
    print("Por favor, insira um número natural não-negativo.")
else:
    # Calcula o fatorial e imprime o resultado
    resultado_fatorial = calcular_fatorial(n)
    print(resultado_fatorial)

