dados = {}
dados['nome'] = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
dados['idade'] = 2023 - ano_nasc
dados['ctps'] = int(input("Carteira de Trabalho: "))
if dados['ctps'] == 0:
    print('=='*30)
    for k,v in dados.items():
        print(f"{k} tem o valor: {v}")
else:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input("Salário: "))
    dados['aposentadoria'] = (35 + (dados['contratação'])) - ano_nasc
    print('=='*30)
    for k,v in dados.items():
        print(f"{k} tem  o valor: {v}")
