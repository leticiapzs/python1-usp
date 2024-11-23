def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def maior_primo(n):
    for num in range(n, 1, -1):
        if eh_primo(num):
            return num

# Exemplos de uso:
print(maior_primo(100))  # Saída esperada: 97
print(maior_primo(7))    # Saída esperada: 7
