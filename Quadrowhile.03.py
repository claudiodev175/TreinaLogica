n = int(input("Digite o fatorial de um número: "))
fator = 1
for x in range(n,0,-1):
    fator *= x
    print("{}".format(fator))
