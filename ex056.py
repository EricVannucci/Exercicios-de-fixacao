print(f"\033[96m{'Analisador completo':^40}\033[m")
print(40 * '+')

velho = 0
nome_velho = ''
nova = 0
media = 0
homem = 0
mulher = 0

# coleta de dados
for c in range(1, 5):
    print(f'------- {c}ª Pessoa -------')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    # tratamento variável sexo
    while sexo != 'm' and sexo != 'f':
        print('\033[31mOpção inválida, digite "M" para masculino ou "F" para feminino\033[m')
        sexo = str(input('Sexo [M/F]: ')).strip().lower()

    # tratamento variável idade
    media += idade
    if sexo == 'f' and idade < 18:
        nova += 1
    elif sexo == 'f':
        mulher += 1
    elif sexo == 'm' and c == 1:
        velho = idade
        nome_velho = nome
        homem += 1
    elif sexo == 'm' and idade > velho:
        velho = idade
        nome_velho = nome

# respostas
print(f'\nA média de idade do grupo é de {media / 4:.0f} anos.')
if homem == 0:
    print('Não existem homens na lista.')
else:
    print(f'O homem mais velho tem {velho} anos e se chama {nome_velho}.')
if mulher == 0:
    print('Não existem mulheres na lista.')
elif nova == 0:
    print('Não existem mulheres menores de 18 anos na lista.')
else:
    print(f'Existe(m) {nova} mulher(es) com menos de 18 anos.')
