print('\033[96m**** Maior e Menor Valor ****\033[m')
print()
media = cont = menor = maior = 0
continuar = 's'
while continuar == 's':
    num = float(input('Digite um número: '))
    cont += 1
    media += num
    if cont == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        elif num <= menor:
            menor = num
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while continuar not in 'sn':
        print('Opção incorreta, digite S para sim ou N para não.')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
print(f'Foram digitados {cont} números;')
if maior == menor:
    print('Todos os números digitados foram iguais! Que falta de criatividade, hein? ;D')
else:
    print(f'O maior número digitado é {maior};')
    print(f'O menor número digitado é {menor};')
print(f'A média dos números digitados é {media / cont:.1f}.')
