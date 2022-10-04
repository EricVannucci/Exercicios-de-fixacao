# menu
print(40 * '*')
print(f"\033[96m{'Comparador de números':^40}\033[m")
print(40 * '*')
um = int(input('Digite um número: '))
dois = int(input('Digite outro número: '))

# resolução
if um < dois:
    print(f'{um} é menor que {dois}')
elif um > dois:
    print(f'{um} é maior que {dois}')
else:
    print('Os dois números são iguais!')
