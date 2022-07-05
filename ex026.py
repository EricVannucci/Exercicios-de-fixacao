frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes.')
print(f'A primeira letra A aparece na posição {frase.find("A")}.')
print(f'A última letra A aparece na posição {frase.rfind("A")}.')
