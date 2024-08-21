medicoes = []
for i in range(4):
    medicao = int(input("Digite a medição de n.{}: ".format(i + 1)))
    medicoes.append(medicao)

for medicao in medicoes:
    if medicao < 110:
        print("{} - Normal".format(medicao))
    elif 110 <= medicao <= 125:
        print("{} - Alterada".format(medicao))
    else:
        print("{} - Muito alta".format(medicao))
media = sum(medicoes) / 4
print("Média das leituras: {:.2f}".format(media))