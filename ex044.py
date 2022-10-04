# menu
print(10 * '\033[96m=\033[m', end=' ')
print('LOJAS GUANABARA', end=' ')
print(10 * '\033[96m=\033[m')
compras = float(input('Qual o valor total das suas compras? R$ '))
print('\nFORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque (10% desc)\n'
      '[2] À vista cartão de débito (8% desc)\n'
      '[3] À vista cartão de crédito (5% desc)\n'
      '[4] 2X no cartão de crédito (5% acrec)\n'
      '[5] 3X ou mais no cartão de crédito (20% acrec)\n'
      '[6] Sair\n')
opcao = int(input('Qual é a opção: '))
while opcao not in [1, 2, 3, 4, 5, 6]:
    opcao = int(input('Qual é a opção? '))

# resultados
if opcao == 1:
    print(f'Comprando R$ {compras:.2f} à vista suas compras saem '
          f'por R$ {compras - (compras * 10 / 100):.2f}!')
elif opcao == 2:
    print(f'Comprando R$ {compras:.2f} à vista no débito suas compras saem '
          f'por R$ {compras - (compras * 8 / 100):.2f}!')
elif opcao == 3:
    print(f'Comprando R$ {compras:.2f} no crédito suas compras saem '
          f'por R$ {compras - (compras * 5 / 100):.2f}!')
elif opcao == 4:
    print(f'Comprando R$ {compras:.2f} em duas vezes, suas compras saem '
          f'por R$ {compras + (compras * 5 / 100):.2f}'
          f' com parcelas de R$ {(compras + (compras * 5 / 100)) / 2:.2f}.')
elif opcao == 5:
    vezes = int(input('Quantas vezes você quer dividir? (máximo 12X): '))
    while 12 < vezes:
        print('\nQuantidade de parcelas inválido, máximo de 12.')
        vezes = int(input('Quantas vezes você quer dividir? '))
    if vezes == 2:
        print(f'Comprando R$ {compras:.2f} em duas vezes, suas compras saem '
              f'por R$ {compras + (compras * 5 / 100):.2f}'
              f' com parcelas de R$ {(compras + (compras * 5 / 100)) / 2:.2f}.')
    elif vezes == 1:
        print(f'Comprando R$ {compras:.2f} em 1 vez no crédito suas compras saem com desconto de 5%.'
              f'\nValor com desconto: R$ {compras - (compras * 5 / 100):.2f}!')
    else:
        print(f'Comprando R$ {compras:.2f} em {vezes}X, suas compras saem por R${compras + (compras * 20 / 100):.2f}, '
              f'sendo a parcela no valor de R${(compras + (compras * 20 / 100)) / vezes:.2f}')
elif opcao == 6:
    print('Obrigado por consultar!')
    exit()
while True:
    continua = str(input('\nDeseja fazer outra consulta? [S/N]')).strip().lower()

# menu repetição
    if continua == 'n':
        print('Obrigado por consultar!')
        exit()
    elif continua == 's':
        print(10 * '\033[96m=\033[m', end=' ')
        print('LOJAS GUANABARA', end=' ')
        print(10 * '\033[96m=\033[m')
        compras = float(input('\nQual o valor total das suas compras? R$ '))
        print('FORMAS DE PAGAMENTO')
        print('[1] À vista dinheiro/cheque (10% desc)\n'
              '[2] À vista cartão de débito (8% desc)\n'
              '[3] À vista cartão de crédito (5% desc)\n'
              '[4] 2X no cartão de crédito (5% acrec)\n'
              '[5] 3X ou mais no cartão de crédito (20% acrec)\n'
              '[6] Sair\n')
        opcao = int(input('Qual é a opção: '))
        while opcao not in [1, 2, 3, 4, 5, 6]:
            opcao = int(input('Qual é a opção? '))

# resultado repetição
        if opcao == 1:
            print(f'Comprando R$ {compras:.2f} à vista suas compras saem por R$ {compras - (compras * 10 / 100):.2f}!')
        elif opcao == 2:
            print(
                f'Comprando R$ {compras:.2f} à vista no débito suas compras saem por '
                f'R$ {compras - (compras * 8 / 100):.2f}!')
        elif opcao == 3:
            print(
                f'Comprando R$ {compras:.2f} no crédito suas compras saem por '
                f'R$ {compras - (compras * 5 / 100):.2f}!')
        elif opcao == 4:
            print(
                f'Comprando R$ {compras:.2f} em duas vezes, suas compras saem por '
                f'R$ {compras + (compras * 5 / 100):.2f}'
                f' com parcelas de R$ {(compras + (compras * 5 / 100)) / 2:.2f}.')
        elif opcao == 5:
            vezes = int(input('Quantas vezes você quer dividir? (máximo 12X): '))
            while 12 < vezes:
                print('\nQuantidade de parcelas inválido, máximo de 12.')
                vezes = int(input('Quantas vezes você quer dividir? '))
            if vezes == 2:
                print(
                    f'Comprando R$ {compras:.2f} em duas vezes, suas compras saem '
                    f'por R$ {compras + (compras * 5 / 100):.2f}'
                    f' com parcelas de R$ {(compras + (compras * 5 / 100)) / 2:.2f}.')
            elif vezes == 1:
                print(f'Comprando R$ {compras:.2f} em 1 vez no crédito suas compras saem com desconto de 5%.'
                      f'\nValor com desconto: R$ {compras - (compras * 5 / 100):.2f}!')
            else:
                print(
                    f'Comprando R$ {compras:.2f} em {vezes}X, suas compras saem '
                    f'por R${compras + (compras * 20 / 100):.2f}, '
                    f'sendo a parcela no valor de R${(compras + (compras * 20 / 100)) / vezes:.2f}')
        elif opcao == 6:
            print('Obrigado por consultar!')
            exit()
