print('\033[96m**** Somador de Números ****\033[m\n')
soma = 0
cont = 0
num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
print(f'Você digitou {cont} número(s) e a soma entre ele(s) é {soma}.')
