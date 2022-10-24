print(40 * '\033[96m=')
print(f"{'Sequencia de Fibonacci':^40}")
print(40 * '=')
print('\033[m')
termos = int(input('Quantos termos você quer mostrar? '))
cont = 2
n = 0
n2 = 1
n3 = n + n2
print('0', end=' → ')
while cont <= termos:
    print(f'{n3}', end=' → ')
    n3 = n + n2
    n = n2
    n2 = n3
    cont += 1
print('Acabou!')
