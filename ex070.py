print(30 * '_')
print(f"\033[96m{'LOJAS SUPER BARATÃO':^30}\033[m")
print(30 * '=')
mais = 's'
soma = mais_mil = menor = cont = 0
barato = ' '
while mais == 's':
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco >= 1000:
        mais_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    mais = ' '
    while mais not in 'sn':
        mais = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if mais == 'n':
        print('-------- FIM DO PROGRAMA --------\n')
print(f'O total das compras foi R$ {soma:.2f}')
if mais_mil == 0:
    pass
else:
    print(f'Temos {mais_mil} produto(s) custando mais de mil Reais.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
