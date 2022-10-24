print('→ \033[96mTabuada v3.0\033[m ←')
print(100 * '\033[96m=\033[m')
while True:
    num = int(input('Tabuada de qual número deseja ver? [digite número negativo para encerrar] '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print(100 * '\033[96m=\033[m')
print('\033[31mVocê encerrou o programa.')
