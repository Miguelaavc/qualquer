'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
dados = {}
galera = []
while True:
    dados.clear()
    dados['nome'] = str(input("Nome: "))
    while True:
        dados['sexo'] = (str(input("Sexo(M/F):")).upper()[0])
        if dados['sexo'] != "M" and dados['sexo'] != "F":
            print('ERRO !!!, Digite somente "M" ou "F".')
        else:
            break
    dados['idade'] = int(input("Idade: "))
    galera.append(dados.copy())
    while True:
        cont = (str(input("Você quer continuar ? (S/N): ")).upper()[0])
        if cont != "S" and cont != "N":
            print('ERRO !!!, Digite somente "S" ou "N".')
        else:
            break
    if cont == "N":
        break
print(galera)
#[{'nome': 'miguel', 'sexo': 'M', 'idade': 16}, {'nome': 'ingrid', 'sexo': 'F', 'idade': 23}]
print(f"Temos {len(galera)} pessoas cadastradas.")