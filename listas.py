alunos = ["Daniel","Eduarda"]
print(alunos)
alunos.append("Gaba")
alunos.append("Clarb")
alunos.append("Zilhão")

print(alunos)
print("o mais foda da lista é {}".format(alunos[3]))
alunos.remove("Gaba")
print(alunos)
alunos.pop()
print(alunos)
tamanho_lista = len(alunos)
print("o tamanho da lista é {}".format(tamanho_lista))
for i in range(len(alunos)):
    print(alunos[i])
