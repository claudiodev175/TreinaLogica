from time import sleep
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
decisão = input("MA , MP ou MH: ")
if (decisão.upper() == "MA"):
    media = (n1 +n2)/2 
elif(decisão.upper() == "MP"):
    media = (n1 * 3.5 + n2 * 7.5) / 11  
elif(decisão.upper() == "MH"):
    media = 2 * n1 * n2 / (n1 +n2)    
print("Calculando...")
sleep(3)
if media >= 7:
    print("Sua média foi {:.2f}, meus parabéns!!".format(media))
else:
    print("Sua média foi {:.2f}, se esforçe mais".format(media))    
    