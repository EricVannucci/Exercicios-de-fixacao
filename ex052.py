print('NÚMEROS PRIMOS\n')
cont = 0
num = int(input('Digite um número para saber se ele é primo: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[96m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if cont == 2:
    print(f'\nO número {num} foi dividido {cont} e por isso é Primo!')
else:
    print(f'\nO número {num} foi dividido {cont} e por isso não é Primo...')
