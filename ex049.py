print('\033[96m*** Tabuada 2.0 ***\033[m')
num = int(input('\nDigite o número que você quer saber a tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c:2} = {num * c}')
