print(12*'=-')
print('Analisador de triângulos')
print(12*'=-')
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if b + c > a and a + c > b and a + b > c:
    print('É possível obter um triângulo com esses seguimentos!')
else:
    print('Não é possível obter um triângulo com esses seguimentos!')
