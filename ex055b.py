print('\033[96mAnalisador de pesos\033[m')
print()
lista = []

for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa em quilos: '))
    lista += [peso]

print(f'\nA pessoa mais leve pesa {min(lista)}Kg.')
print(f'A pessoa mais pesada pesa {max(lista)}Kg.')
