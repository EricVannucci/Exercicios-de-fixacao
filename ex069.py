print(f"{'CADASTRO DE PESSOAS':^25}")

# variáveis
cont = maior18 = homem = mulher_menor_20 = 0

# cadastramento de dados
while True:
    print('\033[96m')
    print('-' * 25)
    print(f"{'CADASTRO PESSOAL':^25}")
    print('-' * 25)
    print('\033[m')
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    cont += 1
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
        if sexo == 'm':
            homem += 1
        elif sexo == 'f' and idade <= 20:
            mulher_menor_20 += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        print(25 * '-')
        break

# dados processados
print(f"Programa encerrado, "
      f"{f'foi cadastrado uma pessoa' if cont == 1 else f'foram cadastrados {cont} pessoas'}.")
# homens
if homem == 1:
    print('Foi cadastrado uma pessoa do sexo masculino.')
elif homem == 0:
    print('Não foi cadastrado nenhuma pessoa do sexo masculino.')
else:
    print(f'Foram cadastrados {homem} pessoas do sexo masculino.')
# mulher menor de 20 anos
if mulher_menor_20 == 1:
    print('Foi cadastrada uma pessoa do sexo feminino abaixo de 20 anos.')
elif mulher_menor_20 == 0:
    print('Não foi cadastrada nenhuma pessoa do sexo feminino com menos de 20 anos.')
else:
    print(f'Foram cadastradas {mulher_menor_20} pessoas do sexo feminino abaixo de 20 anos.')
# pessoas maiores de 18 anos
if maior18 == 1:
    print('Foi cadastrado uma pessoa maior de 18 anos.')
elif maior18 == 0:
    print('Não foi cadastrado nenhuma pessoa maior de 18 anos.')
else:
    print(f'Foram cadastradas {maior18} pessoas com mais de 18 anos.')
