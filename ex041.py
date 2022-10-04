from datetime import date

# intro
print(40 * '>')
print(f"\033[96m{'Classificador de Categorias Natação':^40}\033[m")
print(40 * '<')
nasc = int(input('\nAno de nascimento do atleta: '))

# calculos
data_atual = date.today().year
idade = data_atual - nasc
if idade <= 9:
    print(f'Atleta tem {idade} anos e se enquadra na categoria \033[96mMIRIM')
elif idade <= 14:
    print(f'Atleta tem {idade} anos e se enquadra na categoria \033[96mINFANTIL')
elif idade <= 19:
    print(f'Atleta tem {idade} anos e se enquadra na categoria \03396[mJÚNIOR')
elif idade <= 25:
    print(f'Atleta tem {idade} anos e se enquadra na categoria \033[96mSÊNIOR')
else:
    print(f'Atleta tem {idade} anos e se enquadra na categoria \033[96mMASTER')
