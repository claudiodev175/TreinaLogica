peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

if altura <= 1.50:
    peso_ideal = 50

elif altura <= 1.90:
    peso_ideal = 70

elif altura > 1.90:
    peso_ideal = 100

if peso == peso_ideal:
    print("Parabéns, você está no peso ideal")

elif peso < peso_ideal:
    print("Você precisa engordar {:.3f}kg".format(peso_ideal - peso))
    
elif peso > peso_ideal:
    print("Você precisa emagrecer {:.3f}kg".format(peso - peso_ideal))
