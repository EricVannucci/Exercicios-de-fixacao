from random import choice
n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('Digite o nome de outro aluno: '))
n3 = str(input('Digite o nome de mais um aluno: '))
n4 = str(input('Digite o último nome de um aluno: '))
lista = [n1, n2, n3, n4]
print(f'O aluno escolhido foi: {choice(lista)}')
