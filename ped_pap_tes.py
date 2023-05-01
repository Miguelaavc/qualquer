from random import randint
while True:
    p = int(input('''
    ==================================
    (0) PEDRA                                                             
    (1) PAPEL                       
    (2) TESOURA         
    ==================================
    Escolha sua opção: '''))
    c = randint(0,2)
    
    if p == 0:
        print("Você escolheu PEDRA")
        if c == 0:
            print("\nO computador escolheu PEDRA")
            print("\nEMPATE !!!")
            print('''\n
        ______   
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)

        ______
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 1:
            print("\nO computador escolheu PAPEL")
            print("\nCOMPUTADOR VENCEU !!!")
            print('''\n
        ______   
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)


        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 2:
            print("\nO computador escolheu TESOURA")
            print("\nVOCÊ VENCEU !!!")
            print('''\n
        ______   
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)


        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

    elif p == 1:
        print("Você escolheu PAPEL")
        if c == 0:
            print("\nO computador escolheu PEDRA")
            print("\nVOCÊ VENCEU !!!")
            print('''\n
        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)

    ______   
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 1:
            print("\nO computador escolheu PAPEL")
            print("\nEMPATE !!!")
            print('''\n
        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)

        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 2:
            print("\nO computador escolheu TESOURA")
            print("\nCOMPUTADOR VENCEU !!!")
            print('''\n
        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)

        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

    elif p == 2:
        print("Você escolheu TESOURA")
        if c == 0:
            print("\nO computador escolheu PEDRA")
            print("\nCOMPUTADOR VENCEU !!!")
            print('''\n
        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)

    ______   
    ---'   ____)
        (_____)
        (_____)       
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 1:
            print("\nO computador escolheu PAPEL")
            print("\nVOCÊ VENCEU !!!")
            print('''\n
        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)

        _______
    ---'    ____)____
                ______)
            _______)
            _______)
    ---.__________)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

        elif c == 2:
            print("\nO computador escolheu TESOURA")
            print("\nEMPATE !!!")
            print('''\n
        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)

        _______
    ---'   ____)____
            ______)
            __________)
        (____)
    ---.__(___)
            ''')
            i = str(input("Você quer continuar (S/N)?")).upper()
            if i == "N":
                break

    else:
        print("Opção inválida")
