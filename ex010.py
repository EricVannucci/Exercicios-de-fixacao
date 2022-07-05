real = float(input('Quanto dinheiro você tem na carteira? '))
cotação = float(input('Qual a cotação do dólar de hoje? '))
print(f'Com R${real:.2f} você pode comprar US${real/cotação:.2f}')
