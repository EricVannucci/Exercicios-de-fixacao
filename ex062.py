print('Super gerador de PA v3.0')
print('\033[96m=-\033[m' * 10)
primeiro = int(input('\nQual o primeiro termo: '))
razao = int(input('Qual a razão: '))
cont = 1
termo = primeiro
total = 0
replay = 10
while replay != 0:
    total = replay + total
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('Continua...')
    replay = int(input('Quantos termos mais você gostaria? Digite 0 para encerrar a PA. '))
print('Acabou')
print(f'Foram calculados {total} termos da PA solicitada.')
