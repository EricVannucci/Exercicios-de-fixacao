salario = float(input('Digite o valor do salário para cálculo do aumento: R$ '))
if salario <= 1250.00:
    print(f'Novo salário será de {(salario * 15/100) + salario:.2f}')
else:
    print(f'Novo salário será de {(salario * 10/100) + salario:.2f}')
