print(40 * '\033[96m=\033[m')
print(f"{'10 Termos de uma PA':^40}")
print(40 * '\033[96m=\033[m')

primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo10 = primeiro + 10 * razao

for c in range(primeiro, termo10, razao):
    print(c, end=' → ')
print('Acabou')
