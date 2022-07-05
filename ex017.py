from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hy = (hypot(co, ca))
print(f'O valor da hipotenusa é {hy:.2f}')
