nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em letras minusculas é {nome.lower()}')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
sep = nome.replace(" ", "")
print(f'Seu nome tem {len(sep)} letras.')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras.')

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
