from random import randint
from time import sleep
palpite = 1

# título
print(14 * '-X-')
print(f"\033[96m{'Jogo da Adivinhação v2.0':^40}\033[m")
print(14 * '-X-')

# jogo
jogar = str(input('Vamos jogar? [S/N]: ')).strip().lower()[0]
while jogar not in 'sn':
    jogar = str(input('Vamos jogar? [S/N]: ')).strip().lower()[0]
if jogar == 'n':
    print('\033[31mQue pena... tchau!')
    exit()
else:
    print('\033[35mOba!! Vamos lá, vou pensar em um número entre 1 e 10, tente adivinhar!')
print('Vejamos...')
sleep(2)
print('Já sei!! Digite qual número eu pensei...')
computador = randint(1, 10)

# jogador
jogador = int(input('Qual o seu palpite? '))
while jogador >= 11:
    print('\033[31mNão, não, não!!! Você deve escolher entre 1 e 10!\033[m')
    jogador = int(input('\033[35mQual o seu palpite? '))
while jogador != computador:
    if jogador < computador:
        print('Foi pouco, tente novamente!')
        jogador = int(input('\033[35mTente novamente, qual o seu palpite? '))
        palpite += 1
        while jogador >= 11:
            print('\033[31mNão, não, não!!! Você deve escolher entre 1 e 10!\033[m')
            jogador = int(input('\033[35mQual o seu palpite? '))
    elif jogador > computador:
        print('Foi muito, tente novamente!')
        jogador = int(input('\033[35mTente novamente, qual o seu palpite? '))
        palpite += 1
        while jogador >= 11:
            print('\033[31mNão, não, não!!! Você deve escolher entre 1 e 10!\033[m')
            jogador = int(input('\033[35mQual o seu palpite? '))
if jogador == computador:
    if palpite == 1:
        print(f'\n\033[96mPARABÉNS, você acertou em {palpite} palpite!')
    else:
        print(f'\n\033[96mPARABÉNS, você acertou em {palpite} palpites!')
