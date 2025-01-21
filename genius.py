import random
from time import sleep
import os

# ---------- Funções ----------

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_regras():
    """Exibe as regras do jogo."""
    print('BEM-VINDO AO GENIUS DO PYTHON!')
    sleep(2)
    print('''
As opções de jogo são as seguintes:

vm - vermelho
az - azul
vd - verde
am - amarelo

Digite as respostas separadas por espaços. Exemplo: am am az az vd
''')

def exibir_sequencia(sequencia):
    """Exibe a sequência de cores para o jogador."""
    print("Memorize a sequência:")
    sleep(1)
    for cor in sequencia:
        print(cor, end='    ')
        sleep(1)
    print()
    sleep(1)

def obter_resposta_usuario():
    """Solicita a sequência do usuário."""
    return input('Informe a sequência: ').split()

def verificar_resposta(sequencia, resposta_usuario):
    """Verifica se a resposta do usuário está correta."""
    return resposta_usuario == sequencia

def exibir_resultado(sequencia, pontos, acertou):
    """Exibe o resultado da rodada."""
    if acertou:
        print('Você acertou! Próxima rodada...')
    else:
        print('Você perdeu! A sequência correta era:')
        print(' '.join(sequencia))
        print(f'\nTOTAL DE ACERTOS: {pontos}')
    sleep(2)

# ---------- Variáveis Globais ----------

cores_disponiveis = ['vm', 'az', 'vd', 'am']
sequencia = []
pontos = 0
continuar = 'S'

# ---------- Lógica do Jogo ----------

limpar_tela()
exibir_regras()
input('Pressione ENTER para começar!')
limpar_tela()

while continuar == 'S':
    # Adiciona uma nova cor à sequência
    sequencia.append(random.choice(cores_disponiveis))
    exibir_sequencia(sequencia)

    limpar_tela()
    resposta_usuario = obter_resposta_usuario()

    if verificar_resposta(sequencia, resposta_usuario):
        pontos += 1
        exibir_resultado(sequencia, pontos, True)
    else:
        exibir_resultado(sequencia, pontos, False)
        pontos = 0
        continuar = input('Deseja continuar [S/N]? ').upper().strip()
        sequencia.clear()
    limpar_tela()
