# menu
print(40 * '\033[96m=\033[m')
print(f"{'Conversor de Base Numérica':^40}")
print(40 * '\033[96m=\033[m')
num = int(input('Digite um número inteiro: '))
print('\nEscolha uma base de conversão:')
print('[1] Converter para BINÁRIO\n'
      '[2] Converter para OCTAL\n'
      '[3] Converter para HEXADECIMAL\n')
opcao = int(input('Sua opção: '))

# cálculo
while opcao > 3:
    print('Digite uma opção válida!')
    opcao = int(input('Sua opção: '))
if opcao == 1:
    converter = 'Binário'
    resposta = bin(num)
elif opcao == 2:
    converter = 'Octal'
    resposta = oct(num)
else:
    converter = 'Hexadecimal'
    resposta = hex(num)

# resposta
print(f'O valor {num} convertido para {converter} é {resposta [2:]}')
