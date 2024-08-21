n = int(input("Digite um número de notas: "))
soma = 0
for i in range(n):
    nota = int(input("Digite as notas: "))
    soma += nota
    media = soma / n
print("{:.2f}".format(media))