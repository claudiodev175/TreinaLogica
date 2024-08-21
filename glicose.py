med1 = int(input("Primeira medição: "))
med2 = int(input("Segunda medição: "))
med3 = int(input("Terceira medição: "))
med4 = int(input("Quarta medição: "))

if med1 < 110:
    print("{} - Normal".format(med1))
elif 110 <= med1 <= 125:
    print("{} - Alterada".format(med1))
else:
    print("{} - Muito alta".format(med1))

if med2 < 110:
    print("{} - Normal".format(med2))
elif 110 <= med2 <= 125:
    print("{} - Alterada".format(med2))
else:
    print("{} - Muito alta".format(med2))

if med3 < 110:
    print("{} - Normal".format(med3))
elif 110 <= med3 <= 125:
    print("{} - Alterada".format(med3))
else:
    print("{} - Muito alta".format(med3))

if med4 < 110:
    print("{} - Normal".format(med4))
elif 110 <= med4 <= 125:
    print("{} - Alterada".format(med4))
else:
    print("{} - Muito alta".format(med4))
print("{} - Média das leituras".format((med1 + med2 + med3 + med4) / 4))