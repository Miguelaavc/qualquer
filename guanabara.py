#DESAFIO 36---------------------------------------------------------------- comprar ou nao uma casa

'''vcasa = float(input("Valor da casa: "))
salar = float(input("Salário do comprador: "))
ano = int(input("Em quantos anos: "))
prest_men = vcasa / (12*ano)                                                                    14/8
if prest_men > salar*0.3:                                                                        6 /8 
    print("Empréstimo Negado")
else: 
    print(f"{prest_men:.2f} Reais por mês, durante {ano} anos.")'''

#DESAFIO 37 ------------------------ conversão de bases numericas
# lista_result = []
# lista_hex = ["A", "B", "C", "D", "E", "F"]
# resto = 0

# num = int(input("Número: "))
# num_copy = num 
# base = int(input('''\nQual a base de conversão? 
# "1" para BINÁRIO
# "2" para OCTAL
# "3" para HEXADECIMAL
# \nopção: '''))
# if base == 1:
#     while num_copy != 1:
#         lista_result.append(num_copy%2)
#         num_copy = num_copy//2 
#     lista_result.append(num_copy)                            #CONVERSOR DE BINÁRIO
#     lista_result.reverse()     
#     print(f"{num} em Binário é {lista_result}")
#     print(f"{num} em Binário é", end=" ")
#     for i in lista_result:
#         print(i, end="")

# elif base == 2:
#     if num < 8:
#         print(f"{num} em Octal é {num}")
#     else:
#         while num_copy != 1:
#             lista_result.append(num_copy%8)
#             num_copy = num_copy//8                              #CONVERSOR DE OCTAL
#             if num_copy < 8:
#                 break
#         lista_result.append(num_copy)
#         lista_result.reverse()
#         print(f"{num} em Octal é", end=" ")
#         for i in lista_result:
#             print(i, end="")  

# elif base == 3:
#     if num < 10:
#         print(f"{num} em Hexadecimal é {num}")

#     elif 15 >= num >= 10:
#         #indices     0    1    2    3    4    5                 #COVERSOR DE HEX
#         #lista hex ["A", "B", "C", "D", "E", "F"]
#         #numeros     10   11  12    13   14   15       
#         print(f"{num} em Hexadecimal é {lista_hex[num-10]}")

#     else:
#         while num_copy != 1:
#             resto = num_copy%16
#             if resto > 9:
#                 resto = lista_hex[resto-10]
#             lista_result.append(resto)
#             num_copy = num_copy//16     
#             if num_copy < 16:
#                 break
#         if num_copy > 9:
#             num_copy = lista_hex[num_copy-10]
#         lista_result.append(num_copy)
#         lista_result.reverse()
#         print(f"{num} em Hexadecimal é", end=" ")
#         for i in lista_result:
#             print(i,end="")

# else:
#     print("Opção inválida")

#DESAFIO 45 fazer------------------------

#DESAFIO 46------------------------------------------------------------------fogos de artificio
# from time import sleep
# print("ANO NOVO EM...")
# for i in range (10,0,-1):
#     print(i)
#     sleep(1)
# print('''
#                                    .''.       
#        .''.      .        *''*    :_\/_:     . 
#       :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
#   .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
#  :_\/_:'.:::.    ' *''*    * '.\\'/.' _\(/_'.':'.'
#  : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
#   '..'  ':::'     * /\ *     .'/.\\'.   '
#       *            *..*         :
#      *
#         *
# ''') 

#desafio 47------------------------------------------------------------------pares de 1-50
'''for i in range(2,50,2):
    print(i,end=" ")'''

#desafio 48 -----------------------------------------------------------------soma dos impares de 1-500
'''soma = 0
for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
print(soma)'''

#desafio 49-------------------------------------------------------------------tabuada com laço

#desafio 50------------------------------------------------------------------- soma de 6 numeros pares
soma=0
for i in range (6):
    num = int(input("Número: "))
    if num % 2 == 0:
        soma += num
print(soma)

#desafio 51 -------------------------------------------------------------------


#45 49 51...