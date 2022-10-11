from datetime import date
hoje = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    if (hoje - idade) >= 18:
        maior += 1
    elif (hoje - idade) <= 18:
        menor += 1

print(f'\nExistem {maior} pessoas maiores de idade.')
print(f'Existem {menor} pessoas menores de idade.')
