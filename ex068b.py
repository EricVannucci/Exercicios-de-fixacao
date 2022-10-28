from random import randint
# Título
print('\033[95m=-' * 20)
print(f"{'Vamos jogar PAR ou ÍMPAR!':^40}")
print('-=' * 20, '\033[m')
print()
# contadores
win = loose = cont = 0
novamente = 's'
# Jogadas
while novamente == 's':
    while True:
        computador = randint(1, 11)
        jogador = int(input('Diga um valor: '))
        jogada = str(input('Escolha, Par ou Ímpar? [P/I] ')).strip().lower()[0]
# Análise de jogada válida
        while jogada not in 'pi':
            jogada = str(input('Opção incorreta, escolha PAR (P) ou Ímpar (I)! ')).strip().lower()[0]
# Análise da jogada
        if jogada == 'p' and (computador + jogador) % 2 == 0:
            print('VOCÊ GANHOU!')
            print(f'Você jogou {jogador} e eu joguei {computador}. Total de {jogador + computador}')
            print(20 * '=-')
            win += 1
            cont += 1
        elif jogada == 'p' and (computador + jogador) % 2 == 1:
            print('VOCÊ PERDEU!')
            print(f'Você jogou {jogador} e eu joguei {computador}. Total de {jogador + computador}')
            print(20 * '=-')
            loose += 1
            cont += 1
            novamente = str(input('Deseja jogar novamente? [S/N]: ')).strip().lower()[0]
            while novamente not in 'sn':
                novamente = str(input('Escolha SIM (S) ou NÃO (N): ')).strip().lower()[0]
            if novamente == 'n':
                print(20 * '=-')
                print(f'GAME OVER! \nVocê jogou {cont} vez(es) e venceu {win} partida(s).')
                break
        elif jogada == 'i' and (computador + jogador) % 2 == 1:
            print('VOCÊ GANHOU!')
            print(f'Você jogou {jogador} e eu joguei {computador}. Total de {jogador + computador}')
            print(20 * '=-')
            win += 1
            cont += 1
        elif jogada == 'i' and (computador + jogador) % 2 == 0:
            print('VOCÊ PERDEU!')
            print(f'Você jogou {jogador} e eu joguei {computador}. Total de {jogador + computador}')
            print(20 * '=-')
            loose += 1
            cont += 1
            novamente = str(input('Deseja jogar novamente? [S/N]: ')).strip().lower()[0]
            while novamente not in 'sn':
                novamente = str(input('Escolha SIM (S) ou NÃO (N): ')).strip().lower()[0]
            if novamente == 'n':
                print(20 * '=-')
                print(f'GAME OVER! \nVocê jogou {cont} vez(es) e venceu {win} partida(s).')
                break
