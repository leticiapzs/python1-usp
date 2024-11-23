# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Converte o número em uma string para facilitar a iteração pelos dígitos
numero_str = str(numero)

# Inicializa a variável para armazenar a soma dos dígitos
soma_digitos = 0

# Itera sobre cada dígito na string do número
for digito_str in numero_str:
    # Converte o dígito de volta para um número inteiro e adiciona à soma
    soma_digitos += int(digito_str)

# Imprime a soma dos dígitos
print(soma_digitos)