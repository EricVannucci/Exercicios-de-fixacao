import datetime
ano = int(input('Digite o ano que você quer analisar. Coloque 0 para o ano atual. '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} É BISSEXTO')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO')
