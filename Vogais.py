def vogal(caractere):
    vogais = "aeiouAEIOU"
    return caractere.lower() in vogais

# Exemplos de uso:
print(vogal('a'))  # Saída esperada: True
print(vogal('B'))  # Saída esperada: False
print(vogal('E'))  # Saída esperada: True
print(vogal('z'))  # Saída esperada: False
