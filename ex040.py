# menu
print('\033[96mBoletim Escolar\033[m\n')
nome = str(input('Aluno(a): ')).strip().capitalize()
print(f'insira as notas do aluno(a) {nome}')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

# calculos
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média do aluno {nome} foi {media:.1f}')

# resposta
if media < 5:
    print('\033[31mREPROVADO.')
elif media >= 7:
    print('\033[32mAPROVADO!')
else:
    print('\033[33mRECUPERAÇÃO.')
