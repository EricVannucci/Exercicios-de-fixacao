print(40 * '\033[96m=\033[m')
print(f"{'10 Termos de uma PA':^40}")
print(40 * '\033[96m=\033[m')

primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = primeiro
c = 1

while c <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    c += 1
print('Acabou')
