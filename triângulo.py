l1 = int(input("Digite a primeiro lado do triângulo: "))
l2 = int(input("Digite o segundo lado do triângulo: "))
l3 = int(input("Digite o terceiro lado do triângulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print("Equilátero")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não forma um triângulo")
