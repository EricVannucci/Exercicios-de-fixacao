# questionário
print(40 * '-')
print(f"\033[96m{'Calculadora de IMC':^40}\033[m")
print(40 * '-')
peso = float(input('\nQual seu peso (kg): '))
altura = float(input('Qual sua altura (m): '))

# cálculo
imc = peso / altura**2
print(f'Seu índice de massa corporal (IMC) é de {imc:.1f}.')

# resposta
if imc <= 18.5:
    print('Você está abaixo do seu peso ideal, \033[31mcuidado\033[m!')
elif 18.5 < imc <= 25:
    print('Você está no seu peso ideal, \033[32mparabéns\033[m!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso, \033[33matenção\033[m!')
elif 30 < imc <= 40:
    print('Você está obeso, \033[33matenção\033[m!')
elif imc > 40:
    print('Você está com obesidade mórbida, \033[31mcuidado\033[m!')
