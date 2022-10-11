sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()[0]
while sexo != 'm' and sexo != 'f':
    print('\033[31mDado incorreto, digite "M" para masculino ou "F" para feminino\033[m')
    sexo = str(input('Sexo [M/F]: '))
if sexo == 'm':
    print('Sexo MASCULINO registrado com sucesso!')
else:
    print('Sexo FEMININO registrado com sucesso!')
