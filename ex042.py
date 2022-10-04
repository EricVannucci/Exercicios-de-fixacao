# intro
print(40 * '~')
print(f"\033[96m{'Analisador de Triângulos 2.0':^40}\033[m")
print(40 * '~')

# dados
seg1 = int(input('Digite o primeiro segmento: '))
seg2 = int(input('Digite o segundo seguimento: '))
seg3 = int(input('Digite o terceiro seguimento: '))

# calculos
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos digitados PODEM formar um triângulo! ', end='')
    if seg1 == seg2 == seg3:
        print('O triângulo formado é um EQUILÁTERO')
    elif seg1 != seg2 != seg3 != seg1:
        print('O triângulo formado é um ESCALENO')
    else:
        print('O triângulo formado é um ISÓSCELES')
else:
    print('Os seguimentos digitados NÃO PODEM formar um triângulo!')
