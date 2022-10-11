print(f"\033[96m{'Analisador de pesos:':^40}\033[m")
print(22 * '//')
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa em quilos: '))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'\nA pessoa mais pesada pesa {maior}Kg.')
print(f'A pessoa mais leve pesa {menor}Kg.')
