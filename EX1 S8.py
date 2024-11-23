def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))  # Transforma a lista em um conjunto para remover repetições
    lista_sem_repeticao.sort()  # Ordena a lista sem repetições
    return lista_sem_repeticao

# Exemplo de uso:
lista = [2, 4, 2, 2, 3, 3, 1]
resultado = remove_repetidos(lista)
print(resultado)

lista = [1, 2, 3, 3, 3, 4]
resultado = remove_repetidos(lista)
print(resultado)

