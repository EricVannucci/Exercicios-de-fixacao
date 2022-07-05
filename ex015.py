dia = int(input('Digite quantos dias de aluguel: '))
km = float(input('Digite quantos km rodados: '))
print(f'O valor devido é de R${(dia*60)+(km*0.15):.2f}')
