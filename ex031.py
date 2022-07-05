km = float(input('Qual a distância da sua viagem em KM? '))
print(f'Você está prestes a começar uma viagem de {km} quilômetros!')
if km <= 200:
    print(f'Sua passagem custará R${km*0.50:.2f}')
else:
    print(f'Sua passagem custará R${km*0.45:.2f}')
print('Tenha uma boa viagem!')
