# ---------- Imports ----------

import random
from time import sleep
from random import randint

# ---------- Variáveis ----------
jogadas = 0
cores = ['vm', 'az', 'vd', 'am']
sequencia = []
opcao = []
pontos = 0
continuar = 'S'

# ---------- Lógica ----------

print('BEM VINDO AO GENIUS DO PYTHON!')
sleep(2)
print('''
As opções de jogo são as seguintes:

vm - vermelho
az - azul
vd - verde
am - amarelo

Digite as respostas separadas por espaços. Exemplo: am am az az vd
''')
sleep(3)
comecar = str(input('Pressione ENTER para começar!'))
sleep(2)
print('Vamos lá...')
sleep(3)
print('\n' * 100)
while continuar == 'S':
    sequencia.append(random.choice(cores))
    sleep(1)
    for cor in sequencia:
        print(cor, end = '    ')
        sleep(1)
    sleep(1)
    print('\n' * 100)
    opcao = str(input('Informe a sequência: ')).split()
    # print('Minha opção foi: ', opcao)
    if opcao == sequencia:
        print('Você acertou!')
        sleep(1)
        print('\n' * 100)
        pontos +=1
    else:
        print('Você perdeu! A sequência correta era: ')
        for cor in sequencia:
            print(cor, end = ' ')
        sleep(1)
        print(f'\nTOTAL DE ACERTOS: {pontos}')
        pontos = 0
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
        sequencia.clear()
        print('\n' * 100)