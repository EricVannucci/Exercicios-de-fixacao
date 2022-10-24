print('\033[96mVários números com flag de parada\033[m')
cont = soma = 0
while True:
    num = int(input('Digite um número [use 999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma deles é {soma}.')
