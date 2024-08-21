num = int(input("A Quantidade de notas de um aluno: "))
numerador = 0
for x in range(num):
    x = float(input("Solicitar nota: "))
    numerador += x
    media = numerador / num
print("a média equivale a {:.2f}".format(media))

    