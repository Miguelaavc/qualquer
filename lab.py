geral = []
while True:
    lista = []
    nome = str(input("Nome: "))
    lista.append(nome)
    num = int(input("Número do telefone: "))
    lista.append(num)
    date = int(input("Data de nascimento (dd/mm/aaaa): "))
    lista.append(date)
    geral.append(lista)
    cont = str(input("Você quer continuar ? (S/N)")).upper()
    if cont == "N":
        break
print(geral)
