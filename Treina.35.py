soma = 0
num = 1
den = 1

#while(num < 40):
    #soma += num / den
    #num += 2
    #den *= 2
#print("Soma: {}".format(soma))
for i in range(num, 40 , 2):
    soma += num / den
    num = num + 2
    den = den * 2
print("{}".format(soma))

    

    
               