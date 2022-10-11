print(40 * '\033[96m=\033[m')
print(f"{'Detector de palíndromo':^40}")
print(40 * '\033[96m=\033[m')

frase = str(input('\nDigite uma frase: ')).strip().upper()
contra = frase[::-1]

print(f'A frase \033[96m{frase}\033[m escrita ao contrário é \033[96m{contra}\033[m')
if frase.replace(' ', '') == contra.replace(' ', ''):
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
