from random import randint
# Título
print(20*'\033[96m=-')
print(f"{'Vamos jogar par ou ímpar?':^40}")
print(20*'=-')
print('\033[m')
cont = 0
win = 0
# inicio do jogo
while True:
    computador = randint(1, 11)
    jogador = int(input('Me diga um valor: '))
    jogada = str(input('Par ou Ímpar? [P/I]: ')).lower().strip()[0]
# validação da jogada
    while jogada not in 'pi':
        print('Opção inválida! Tente novamente...')
        jogada = str(input('Use "P" para Par ou "I" para Ímpar. '))
# Análise das jogadas
    if jogada == 'p' and (jogador + computador) % 2 == 0:
        print(f'Você jogou {jogador} e eu joguei {computador}, total de {jogador + computador}. '
              f'Deu PAR')
        print('\033[32mVocê Ganhou!!\033[m')
        cont += 1
        win += 1
        print(20 * '\033[96m=-')
        print('\033[m')
    elif jogada == 'p' and (jogador + computador) % 2 == 1:
        print('\033[31mVocê Perdeu!')
        print(20 * '\033[96m=-')
        cont += 1
        break
    elif jogada == 'i' and (jogador + computador) % 2 == 1:
        print(f'Você jogou {jogador} e eu joguei {computador}, total de {jogador + computador}. '
              f'Deu ÍMPAR')
        print('\033[32mVocê Ganhou!!\033[m')
        cont += 1
        win += 1
        print(20 * '\033[96m=-')
        print('\033[m')
    elif jogada == 'i' and (computador + jogador) % 2 == 0:
        print('\033[31mVocê Perdeu!')
        print(20 * '\033[96m=-')
        cont += 1
        break
# Finalização do jogo e placar
print(f'\n\033[94mGAME OVER! Você ganhou {win} vez(es) em {cont} jogada(s)...')
