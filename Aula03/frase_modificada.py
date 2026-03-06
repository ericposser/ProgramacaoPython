frase = input("digite uma frase: ")
print("a frase possui: ", len(frase), "caracteres")
print("a frase originial: ", frase)
print("a frase maiusculo: ", frase.upper())
print("a frase minusculo: ", frase.lower())

frase_modificada = frase.replace('a', '@').replace('e', '8')
print("a frase com 'a' por '@' e 'e' por '8': ", frase_modificada)
