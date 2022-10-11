print('\033[31m----> Analisador de Números <----\033[m')
num1 = float(input('\nDigite um número: '))
num2 = float(input('Digite outro número: '))
print('\033[96mO que você deseja fazer com esses números?\n')
print('[1] Soma\n'
      '[2] Multiplicação\n'
      '[3] Maior\n'
      '[4] Novos números\n'
      '[5] Sair do programa\n')
opcao = int(input('Escolha uma opção: \033[m'))

while True:
    if opcao == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}.\n')
    elif opcao == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}.\n')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}.\n')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}.\n')
        else:
            print(f'{num1} e {num2} são iguais!\n')
    elif opcao == 4:
        print('Escolha novos números:')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite mais um número: '))
        print('O que deseja fazer agora?\n')
    elif opcao == 5:
        print('\033[31mVocê escolheu sair do programa, tchau!!')
        exit()
    print('\033[96m[1] Soma\n'
          '[2] Multiplicação\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    opcao = int(input('O que você deseja fazer agora? \033[m'))
