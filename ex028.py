from random import randint
from time import sleep
print(11*'=-')
print('Advinhador de Números!')
print(11*'-=')
print('Estou pensando em um número....')
sleep(3)
num = int(input('Escolha um número de 0 a 10: '))
comp = randint(0, 10)
if num == comp:
    print('Parabéns, você ganhou!')
else:
    print(f'Você perdeu, eu escolhi {comp}')
