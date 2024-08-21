peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura ** 2
print("O seu IMC é {:.2f}".format(imc))
if imc <= 20:
    print("Você está abaixo do peso normal")
elif imc > 20 and imc <= 25:
    print("Você está no peso ideal, parabéns!!") 
elif imc > 25 and imc <= 30:
    print("Você está levemente acima do peso")
elif imc > 30 and imc <= 40:
    print("Você está obeso")
else:
    print("Você está com obesidade mórbida")