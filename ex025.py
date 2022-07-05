nome = str(input('Digite seu nome completo: ')).strip().upper()
#lista = nome.split()
print(f'Seu nome possui Silva? {nome.__contains__("SILVA")}')

nom = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome possui Silva? {"SILVA" in nom.upper()}')
