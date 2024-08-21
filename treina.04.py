from time import sleep
print("Vamos calcular o volume de um cilindro")
sleep(3)
r = float(input("Digite o raio do cilindro: "))
h = float(input("Digite a altura do cilindro: "))
print("Calculando...")
sleep(3)
print("A area do cilindro equivale a {:.3}".format(3.14 * r ** 2 * h))