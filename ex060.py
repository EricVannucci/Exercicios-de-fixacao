from math import factorial
from time import sleep

print(40 * '\033[96m*\033[m')
print(f"{'Calculadora de Fatorial':^40}")
print(40 * '\033[96m*\033[m')

num = int(input('\nDigite um número inteiro para calcular seu fatorial: '))
print(f'Calculando {num}!')
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\n', end='')
sleep(1)
for c in range(num, 1, -1):
    print(c, end=' x ')
print(f'1 = {factorial(num)}')
