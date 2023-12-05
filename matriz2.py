matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("Matriz antes da multiplicação:")
for linha in matriz:
    print(linha)

k = int(input("Digite o valor de k: "))

for i in range(3):
    matriz[i][i] *= k


print("Matriz depois da multiplicação:")
for linha in matriz:
    print(linha)