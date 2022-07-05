from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {ang}º tem o SENO de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang}º tem o COSSENO de {cos(radians(ang)):.2f}')
print(f'O ângulo de {ang}º tem a TANGENTE de {tan(radians(ang)):.2f}')
