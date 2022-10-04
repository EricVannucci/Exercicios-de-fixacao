soma = 0
cont = 0

print(f"\033[96m{'>>>> Digite 6 valores: <<<<':^40}\033[m\n")
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'\n\033[96mForam digitados {cont} valor(es) par(es) e a soma dele(s) é {soma}.')
