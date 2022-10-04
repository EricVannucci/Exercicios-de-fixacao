from datetime import date

# menu
print(20 * '\033[32mX-')
print(f"\033[92m{'ALISTAMENTO MILITAR':^39}\033[m")
print(20 * '\033[32mX-\033[m')
data_atual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = data_atual - nascimento

# respostas
if idade == 18:
    print('Aliste-se imediatamente!')
elif idade >= 18:
    print(f'Já se passaram {idade - 18} anos do seu alistamento.\n'
          f'Seu alistamento foi em {data_atual - (idade - 18)}.')
elif idade <= 17:
    print(f'Ainda faltam {18 - idade} anos para seu alistamento.\n'
          f'Seu alistamento será em {data_atual + (18 - idade)}, fique atento!')
