geral = []
while True:
    opcao= int(input('''\n========= MENU =========
1. CADASTRAR          2. GERAL
3. PESQUISAR          4. EXCLUIR
5. SAIR
escolha sua opção: '''))
    if opcao == 1:
        lista = []
        nome = str(input("Nome: "))
        lista.append(nome)
        num = str(input("Número do telefone: "))
        lista.append(num)
        date = str(input("Data de nascimento (dd/mm/aaaa): "))
        lista.append(date)
        geral.append(lista)
        print(f"\n{nome} foi CADASTRADO!")

    elif opcao == 2:
        var = open("dados.txt", "w")
        #var.write()
        for pessoas in range((len(geral))):
            print("\n")
            for dados in geral[pessoas]:
                #print(f"{dados}")
                #for i in range(2):
                    var.write(dados)

    elif opcao == 3:
        #procurar o nome na linha do arquivo
        pass

    elif opcao == 4:
        #remover pelo nome
        pass

    elif opcao == 5:
        break
