print('\033[96m**** Maior e Menor Valor ****\033[m')
print()
media = cont = 0
numeros = []
continuar = 's'
while continuar == 's':
    num = float(input('Digite um número: '))
    cont += 1
    media += num
    numeros += [num]
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while continuar not in 'sn':
        print('Opção incorreta, digite S para sim ou N para não.')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
print()
print(f'O maior número digitado é {max(numeros)};')
print(f'O menor número digitado é {min(numeros)};')
print(f'Foram digitados {cont} números e a média dos números digitados é {media / cont:.1f}.')
