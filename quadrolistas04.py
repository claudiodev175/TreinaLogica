numeros = []

while(True):
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(media)    