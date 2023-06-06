import random


# Função que verifica o pH do solo
def escolha_neutralizador():

    acidos = ["Ácido Cítrico","Vinagre Diluído","Enxofre", "Ácido Sulfúrico"]
    alcalinos = ["Calcário Dolomítico","Cinza de Madeira","Calcário Calcítico","Hidróxido de Cálcio"]
    pH = random.randrange(15)

    if pH < 6:
        print('Jogando solucao alcalina neutralizadora')
    elif pH > 6:
        print('Jogando solucao acida neutralizadora')
    else:
        print('Solo esta com pH adequado!')

    while True:
        if pH > 6:
            print(f'pH so seu solo = {pH}')
            pH = pH - 0.5
        elif pH < 6:
            print(f'pH so seu solo = {pH}')
            pH = pH + 0.5
        else:
            print(f'pH do solo = {pH}, solo neutralizado')
            break




# Função com menus para saber mais sobre os neutralizadores de pH
def saibaMais():
    while True:

        print('''
        Escolha a categoria de neutralizadores que deseja saber

        1 - Ácidos

        2 - Básicos

        ''')

        escolhaCategoriaNeutralizador = int(input("Digite sua escolha: "))

        if escolhaCategoriaNeutralizador == 1:
            print('''
            Escolha o neutralizador ácido para saber mais:

            1 - Ácido Cítrico

            2 - Vinagre Diluído

            3 - Enxofre

            4 - Ácido Sulfúrico

            ''')
            escolhaAcido = int(input("Digite sua Escolha: "))

            if escolhaAcido == 1:
                print("O Ácido Cítrico é um ácido suave que pode ajudar a diminuir o pH do solo. Pode ser encontrado em forma de pó ou líquido.")
            elif escolhaAcido == 2:
                print("O vinagre contém ácido acético, que pode ajudar a reduzir o pH do solo. Use vinagre branco destilado e dilua-o em água antes de aplicar no solo. ")
            elif escolhaAcido == 3:
                print("Adicionar enxofre elemental ao solo pode ajudar a diminuir o pH, pois o enxofre reage com a água e forma ácido sulfúrico.")
            elif escolhaAcido == 4:
                print("É um ácido forte e eficaz para diminuir o pH do solo, mas deve ser usado com cautela, pois pode ser perigoso e corrosivo. Recomenda-se consultar um especialista antes de utilizá-lo.")
            
        elif escolhaCategoriaNeutralizador == 2:
            print('''
            Escolha o neutralizador Básicos:

            1 - Calcário Dolomítico

            2 - Cinza de Madeira

            3 - Calcário Calcítico

            4 - Hidróxido de Cálcio

            ''')
            escolhaBasico = int(input("Digite sua escolha: "))

            if escolhaBasico == 1:
                print(" É uma forma comum de corretivo de solo, que contém carbonato de cálcio e magnésio. Ajuda a aumentar o pH do solo de forma gradual.")
            elif escolhaBasico == 2:
                print("A cinza de madeira proveniente de lareiras ou fogões a lenha é uma fonte natural de potássio e outros minerais. Também tem a capacidade de elevar o pH do solo.")
            elif escolhaBasico == 3:
                print("Similar ao calcário dolomítico, o calcário calcítico é uma opção para aumentar o pH do solo. Contém principalmente carbonato de cálcio.")
            elif escolhaBasico == 4:
                print("Conhecido como cal hidratada, pode ser usado para elevar o pH do solo. É necessário ter cuidado ao aplicá-lo, pois é um composto forte.")









while True:
    print('''
    Escolha o que deseja fazer:

    0 - Encerrar Programa

    1 - Verificar pH do solo
    
    2 - Saiba mais sobre os neutralizadores!
    
    ''')
    
    opcaoPrograma = int(input('Digite sua escolha: '))

    if opcaoPrograma == 0:
        break
    elif opcaoPrograma == 1:
        escolha_neutralizador()
    elif opcaoPrograma == 2:
       saibaMais()
            