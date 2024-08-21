from time import sleep
print("Vamos calcular o volume de um cone")
sleep(3)
r = float(input("Digite o raio do cone: "))
h = float(input("Digite a altura do cone: "))
print("Calculando...")
sleep(3)
print("A area do cone equivale a {:.3}".format(0.33 * 3.14 * r**2 * h))