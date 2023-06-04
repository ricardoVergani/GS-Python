import random

def escolha_neutralizador():
    pH = random.randrange(1,14)

    if pH < 5:
        print('Jogando solucao alcalina neutralizadora')
    elif pH > 6.5:
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

while True:
    print('''
    Escolha o seu tipo de plantação:

    1 - Tomate
    
    ''')
    
    escolha = int(input('Digite sua escolha: '))

    if escolha == 0:
        break
    elif escolha == 1:
        escolha_neutralizador()