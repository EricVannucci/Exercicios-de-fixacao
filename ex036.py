# tela de boas-vindas
print('**** \033[96mSimulador de Empréstimos\033[m ****')

# inserindo dados
casa = float(input('Digite o valor da casa desejada:R$ '))
salario = float(input('Digite o salário atual:R$ '))
anos = int(input('Em quantos anos deseja pagar: '))
parcela = casa / (anos * 12)

# calculos
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${parcela:.2f}')
if parcela >= salario * 30 / 100:
    print('O empréstimo NÃO poderá ser concedido')
else:
    print('O empréstimo SERÁ concedido')
