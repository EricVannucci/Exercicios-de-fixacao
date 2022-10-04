from random import randint
from time import sleep
import pygame

# título
print(40 * '\033[36m#\033[m')
print(f"\033[96m{'Vamos jogar PEDRA, PAPEL, TESOURA?':^40}\033[m")
print(40 * '\033[36m#\033[m')
pygame.init()
pygame.mixer.music.load('bridgezone.mp3')
pygame.mixer.music.play()

# contadores placar e definição das opções
vitorias = derrotas = empates = 0
itens = ('Pedra', 'Papel', 'Tesoura')

while True:

    # menu
    jogar = str(input('Quer jogar? [S/N] ')).strip().lower()
    if jogar == 's':
        print('+------------+\n'
              '|[0] PEDRA   |\n'
              '|[1] PAPEL   |\n'
              '|[2] TESOURA |\n'
              '+------------+\n')
        jogador = int(input('Sua escolha é: '))
        while jogador not in [0, 1, 2]:
            print('Escolha inválida, tente novamente!')
            jogador = int(input('Sua escolha é: '))
        computador = randint(0, 2)
        print('\033[94mJo\n')
        sleep(1)
        print('\033[34mKen\n')
        sleep(1)
        print('\033[36mPô!\n\033[m')
        sleep(1)

        # definição das jogadas
        print(f'O jogador escolheu {itens[jogador]}!')
        print(f'O computador escolheu {itens[computador]}!\n')

        # verificação das jogadas
        if computador == jogador:
            print('\033[33mEmpate!\033[m')
            empates += 1
        elif computador == 0 and jogador == 1:
            print('\033[32mVocê ganhou!\033[m')
            vitorias += 1
        elif computador == 0 and jogador == 2:
            print('\033[31mVocê perdeu!\033[m')
            derrotas += 1
        elif computador == 1 and jogador == 0:
            print('\033[32mVocê ganhou!\033[m')
            vitorias += 1
        elif computador == 1 and jogador == 2:
            print('\033[31mVocê perdeu!\033[m')
            derrotas += 1
        elif computador == 2 and jogador == 0:
            print('\033[32mVocê ganhou!\033[m')
            vitorias += 1
        elif computador == 2 and jogador == 1:
            print('\033[31mVocê perdeu!\033[m')
            derrotas += 1

    # finalizando e placar
    elif jogar == 'n':
        print('Que pena... TCHAU!!')
        print('\033[96m### PLACAR ###')
        print(f'\033[32m[{vitorias}] Vitórias\033[m\n'
              f'\033[33m[{empates}] Empates\033[m\n'
              f'\033[31m[{derrotas}] Derrotas\033[m\n')
        exit()
