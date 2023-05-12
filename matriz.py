lista = []
matriz = []
with open("arq.txt", "r") as arq:
    for linha in arq:
        lista.append((linha.strip()).split())

for i in range(int(lista[0][0])): # LINHAS
    matriz.append((int(lista[0][1]) * "1 ").split()) #COLUNAS

for indicelista in range(1, len(lista)):
    matriz[int(lista[indicelista][0])][int(lista[indicelista][1])] = "0"
    
for linhamatriz in matriz:
    print(linhamatriz)
