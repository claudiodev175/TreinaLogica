from time import sleep
duração = int(input("Digite a duração de um evento em uma fábrica em segundos: "))
print("Calculando...")
sleep(3)

#Cálculo das horas
hora = duração // 3600
resto_horas = duração % 3600

#Cálculo dos minutos
minuto = resto_horas // 60
resto_minuto = resto_horas % 60

#Cálculo dos segundo
segundo = resto_minuto

#Exibição
print("HH:MM:SS = {}:{}:{}".format(hora , minuto , segundo))