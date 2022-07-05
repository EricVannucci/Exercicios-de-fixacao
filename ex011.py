h = float(input('Digite qual a altura da parede: '))
c = float(input('Digite qual o comprimento da parede: '))
a = h*c
print(f'Sua parede mede {h:.2f}x{c:.2f} e sua área é de {a:.3f}m².')
print(f'Para pintar sua parede serão necessários {a/2:.3f} litros de tinta.')
