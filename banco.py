geral = []
conta = []
num = 1
cont = 1
while True:
    print("""\n############### MENU PRINCIPAL ###############
    1. Criar Conta        2. Mostrar Saldo
    3. Depósito           4. Saque
    5. Transferência      6. Relatório Geral
    0. Sair
    ----------------------------------------
    """)
    op = int(input("Digite sua opção -> "))
    if op == 1:
        print("## CRIAR CONTAS ##")
        nome_1 = str(input("Nome do titular da conta: "))
        valor_1 = float(input("Valor de depósito inicial: "))
        conta.append([nome_1, valor_1])
        print(f"O número da conta é: {conta.index(conta[cont-1])+1}")
        geral = conta
        cont+=1
    
    elif op == 2:
        print("## MOSTRAR SALDO ##")
        num = int(input("Número da conta: "))
        print(f"\nTitular: {geral[(num-1)][0]} ")
        print(f"Saldo: {geral[(num-1)][1]}")

    elif op == 3:
        print("## DEPÓSITO ##")
        num = int(input("Número da conta: "))
        dep = float(input("Valor a ser depositado: "))
        geral[(num-1)][1] = geral[(num-1)][1] + dep

    elif op == 4:
        print("## SAQUE ##")
        num = int(input("Número da conta: "))
        saq = float(input("Valor a ser sacado: "))
        geral[(num-1)][1] = geral[(num-1)][1] - saq

    elif op == 5:
        print("## TRANSFERÊNCIA ##")
        num = int(input("Número da conta de transferência: "))
        valor_de_transf = float(input("Valor para transferir: "))
        geral[(num-1)][1] = (geral[(num-1)][1]) -  valor_de_transf
        num = int(input("Número da conta de recebimento: "))
        geral[(num-1)][1] += valor_de_transf

    elif op == 6:
        cont = 1
        print("teste apaga ai dps")
        print("## RELATÓRIO GERAL ##")
        print(f"\nQuantidade de contas: {len(geral)}")
        for i in geral:
            print(f"\nTitular: {geral[(num-1)][0]}")
            print(f"Saldo: {geral[(num-1)][1]}")
            print(f"Número da conta: {conta.index(conta[cont-1])+1}")
        
    elif op == 0:
        print("Programa Encerrado !!!")
        break
    
#alteração massa
