from random import randint
from time import sleep
cont = ""
regis = ""
num = 13298755
while True:
    print("========================================")
    print(f"Número: {num}")
    regis = str(input("Registrado: ")).upper()
    print("Carregando...")
    sleep (randint(1,2))
    print("Registrando...")
    sleep (randint(1,2))
    print('''   
    ---------------------------
        TUDO CERTO.
        BOA PALESTRA !!!
    ---------------------------
    ''')
    cont = str(input("Continuar ?(S|N)")).upper()
    print('''
    
    ''')
    num += 1
    if cont == "N":
        break
    else: 
        pass
