velo = int(input('Digite a velocidade apurada em KM/h: '))
if velo > 80:
    print(f'Você foi multado, está a {velo-80} KM/h acima do limite!')
    multa = (velo-80)*7
    print(f'O valor a pagar da multa é: R${multa:.2f}')
else:
    print('Parabéns, você está dentro dos limites de velocidade da via!')
print('Tenha um bom dia, dirija com cuidado!')
