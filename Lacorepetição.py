n = int(input("Digite a quantidade de interações: "))

#Inicialização
contador = 0

#Verificação do Critério de Parada
while(contador < n):
    print(n)
    contador += 1#atualização


for contador in range(0,n,2):
    print(contador)