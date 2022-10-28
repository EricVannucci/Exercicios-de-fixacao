from random import randint
# Título
print('\033[95m=-' * 20)
print(f"{'Vamos jogar PAR ou ÍMPAR!':^40}")
print('-=' * 20, '\033[m')
cont = win = 0
print()
while True:
    computador = randint(1, 11)
    jogador = int(input('Diga um número: '))
    soma = computador + jogador
    jogada = ' '
    while jogada not in 'pi':
        jogada = str(input('Par ou Ímpar? [P/I] ')).lower().strip()[0]
        print(f'Você jogou {jogador} e eu joguei {computador}, a soma é {soma}.', end=' ')
        print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
        print(20 * '-=')
    if jogada == 'p':
        if soma % 2 == 0:
            print('Você Ganhou!!')
            print(20 * '=-')
            cont += 1
            win += 1
        else:
            print('Você Perdeu!!')
            print(20 * '-=')
            cont += 1
            break
    if jogada == 'i':
        if soma % 2 == 1:
            print('Você Ganhou!!')
            print(20 * '-=')
            cont += 1
            win += 1
        else:
            print('Você Perdeu!!')
            print(20 * '=-')
            cont += 1
            break
print(f'\nGAME OVER!!! Você jogou {cont} partida(s) e ganhou {win} vez(es)!')
