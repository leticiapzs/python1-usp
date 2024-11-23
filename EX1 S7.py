largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

for i in range(altura):
    for j in range(largura):
        print('#', end='')
    print()  # Adiciona uma quebra de linha após cada linha do retângulo
