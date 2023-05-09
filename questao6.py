with open('arq1.txt','r') as file:
    for linha in file:
        lista.append(linha[::-1].strip())
lista.reverse()
with open("arq2.txt","w") as arq2:
    for frase in lista:
        arq2.write(frase + "\n")
