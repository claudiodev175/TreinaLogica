n = int(input("Digite a quantidade de notas: "))
notas = []
soma = 0
for i in range (n):
    nota = int(input("Digite a nota n.{}: ".format(i + 1)))
    notas.append(nota)
    media = sum(notas) / n
print("A Média das notas foi {:.2f}".format(media))
