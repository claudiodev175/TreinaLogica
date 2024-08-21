palavra = input("Digite uma palavra: ")
contador = 0
for letra in palavra:
    if letra == "B" or letra == "b":
        contador += 1
        print("a palavra '{}' possui {} letra(s) 'b'".format(palavra,contador))