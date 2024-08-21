idade = int(input("Digite a idade do paciente :"))
peso = float(input("Digite o peso do paciente (kg): "))

if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    else:
        dosagem = 875
else:
    if 5 < peso <= 9:
        dosagem = 125
    elif 9 < peso <= 16:
        dosagem = 250
    elif 16 < peso <= 24:
        dosagem = 375
    elif 24 < peso <= 30:
        dosagem = 500
    else:
        dosagem = 750

qtde_degotas = dosagem * 20 / 500

print("{} gotas".format(qtde_degotas))
