n = int(input("Digite o valor de N: "))

if 0 < n < 46:
    n1 = 0
    n2 = 1
    print("{} {}".format(n1,n2), end=" ")
    for i in range(n - 2):
        t = n1 + n2
        print(t , end=" ")
        n1 = n2
        n2 = t

else:
    print("O valor de N é inválido")