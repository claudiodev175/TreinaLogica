n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

menor = min(n1 , n2)
maior = max(n1 , n2)

contador = 0
for i in range(menor , maior + 1):
    if i % 2 == 0:
        contador += 1
print(f"Quantidade de números pares: {contador}")

#if n2 > n1:
   # for x in range(n1 , n2):
     #   if x % 2 == 0:
     #       print(x)
#if n1 > n2:
   # for x in range(n2 , n1):
        #if x % 2 == 0:
        #   print(x)


     
