import random


# Função que verifica o pH do solo
def escolha_neutralizador():

    # Listas com neutralizadores ácidos e bases em ordem crescente de força
    acidos = ["Ácido Cítrico","Vinagre Diluído","Enxofre", "Ácido Sulfúrico"]
    alcalinos = ["Calcário Dolomítico","Cinza de Madeira","Calcário Calcítico","Hidróxido de Cálcio"]

    # Gera um pH aleatório entre 0 e 14
    pH = random.randrange(15)

    print(f'''         
    ----------------------------------------------------
    
          
    Valor de pH adequado para seu solo: entre 5.5 e 6.5
    pH do seu solo = {pH}


    ----------------------------------------------------
    ''')

    # Libera o neutralizador correspondente ao pH
    if pH < 2:
        print(f'Jogando solução alcalina neutralizadora - {alcalinos[3]}')
        print()
    elif pH >= 2 and pH < 3:
        print(f'Jogando solução alcalina neutralizadora - {alcalinos[2]}')
        print()
    elif pH >= 3 and pH < 4:
        print(f'Jogando solução alcalina neutralizadora - {alcalinos[1]}')
        print()
    elif pH >= 4 and pH < 5.5:
        print(f'Jogando solução alcalina neutralizadora - {alcalinos[0]}')
        print()
    elif pH > 6.5 and pH <= 8:
        print(f'Jogando solução ácida neutralizadora - {acidos[0]}')
        print()
    elif pH > 8 and pH <= 10:
        print(f'Jogando solução ácida neutralizadora - {acidos[1]}')
        print()
    elif pH > 10 and pH <= 12:
        print(f'Jogando solução ácida neutralizadora - {acidos[2]}')
        print()
    elif pH > 12 and pH <= 14:
        print(f'Jogando solução ácida neutralizadora - {acidos[3]}')
        print()

    else:
        print('\033[32mSolo esta com pH adequado!\033[m')

    while True:
        if pH > 6.5:
            print(f'pH do seu solo = {pH}')
            pH = pH - 0.5
        elif pH < 5.5:
            print(f'pH do seu solo = {pH}')
            pH = pH + 0.5
        else:
            print(f'''pH do seu solo = {pH}
                  

            \033[32mSolo neutralizado com sucesso!\033[m
                  
            ''')
            break


# Função com menus para saber mais sobre os neutralizadores de pH
def saibaMais():
    while True:
        try:
            print('''            
            ----------------------------------------------------


            \033[34mEscolha a categoria de neutralizadores que deseja saber

            1 - Ácidos

            2 - Básicos\033[m

            
            ----------------------------------------------------
            ''')

            escolhaCategoriaNeutralizador = int(input("\033[33mDigite sua escolha:\033[m "))
            print()

            if escolhaCategoriaNeutralizador == 1:
                categoriaAcidos()
                break
            
            elif escolhaCategoriaNeutralizador == 2:
                categoriaBasicos()
                break
            else:
                print("\033[31mDigite 1 ou 2 para ser uma opção válida!\033[m\n")
        except ValueError:
            print("\033[31mDigite um número inteiro!\033[m\n")
        except Exception:
            print("\033[31mOcorreu um erro inesperado!\033[m\n")

# Função com opções de ácidos e suas explicações
def categoriaAcidos():
    while True:
        try:
            print('''            
            ----------------------------------------------------


            \033[34mEscolha o neutralizador ácido para saber mais:

            1 - Ácido Cítrico

            2 - Vinagre Diluído

            3 - Enxofre

            4 - Ácido Sulfúrico\033[m


            ----------------------------------------------------
            ''')
            escolhaAcido = int(input("\033[33mDigite sua escolha:\033[m "))
            print()

            if escolhaAcido == 1:
                print("O Ácido Cítrico é um ácido suave que pode ajudar a diminuir o pH do solo. Pode ser encontrado em forma de pó ou líquido.\n")
                break
            elif escolhaAcido == 2:
                print("O vinagre contém ácido acético, que pode ajudar a reduzir o pH do solo. Use vinagre branco destilado e dilua-o em água antes de aplicar no solo.\n")
                break
            elif escolhaAcido == 3:
                print("Adicionar enxofre elemental ao solo pode ajudar a diminuir o pH, pois o enxofre reage com a água e forma ácido sulfúrico.\n")
                break
            elif escolhaAcido == 4:
                print("É um ácido forte e eficaz para diminuir o pH do solo, mas deve ser usado com cautela, pois pode ser perigoso e corrosivo. Recomenda-se consultar um especialista antes de utilizá-lo.\n")
                break
            else: 
                print("\033[31mEscolha 1, 2, 3 ou 4 para a opção ser válida!\033[m\n")
        except ValueError:
            print("\033[31mDigite um número inteiro!\033[m\n")
        except Exception:
            print("\033[31mOcorreu um erro inesperado!\033[m\n")

# Função com opções de bases e suas explicações
def categoriaBasicos():
    while True:
        try:
            print('''             
            ----------------------------------------------------


            \033[34mEscolha o neutralizador Básicos:

            1 - Calcário Dolomítico

            2 - Cinza de Madeira

            3 - Calcário Calcítico

            4 - Hidróxido de Cálcio\033[m


            ----------------------------------------------------
            ''')
            escolhaBasico = int(input("\033[33mDigite sua escolha:\033[m "))
            print()

            if escolhaBasico == 1:
                print(" O calcário dolomítico consegue fazer a correção de solo, que contém carbonato de cálcio e magnésio. Ajuda a aumentar o pH do solo de forma gradual.")
                break
            elif escolhaBasico == 2:
                print("A cinza de madeira proveniente de lareiras ou fogões a lenha é uma fonte natural de potássio e outros minerais. Também tem a capacidade de elevar o pH do solo.")
                break
            elif escolhaBasico == 3:
                print("Similar ao calcário dolomítico, o calcário calcítico é uma opção para aumentar o pH do solo. Contém principalmente carbonato de cálcio.")
                break
            elif escolhaBasico == 4:
                print("Conhecido como cal hidratada, pode ser usado para elevar o pH do solo. É necessário ter cuidado ao aplicá-lo, pois é um composto forte.")
                break
            else:
                print("\033[31mEscolha 1, 2, 3 ou 4 para uma opção válida!\033[m\n")
        except ValueError:
            print("\033[31mDigite um número inteiro!\033[m\n") 
        except Exception:
            print("\033[31mOcorreu um erro inesperado!\033[m\n")


while True:
    try:
        print('''            
        ----------------------------------------------------

        
        \033[34mEscolha o que deseja fazer:

        0 - Encerrar Programa

        1 - Verificar pH do solo
    
        2 - Saiba mais sobre os neutralizadores!\033[m
    
        
        ----------------------------------------------------
        ''')
    
        opcaoPrograma = int(input('\033[33mDigite sua escolha:\033[m '))
        print()

        if opcaoPrograma == 0:
            break
        elif opcaoPrograma == 1:
            escolha_neutralizador()
        elif opcaoPrograma == 2:
            saibaMais()
        else:
            print("\033[31mDigite 0, 1 ou 2 das opções disponíveis!\033[m")
    except ValueError:
        print("\033[31mDigite um número inteiro!\033[m")
    except Exception:
        print("\033[31mOcorreu um erro inesperado!\033[m")