import random

def popular_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(100, 400))
    return lista

def exibir_lista(lista):
    print("lista:", lista)

def remover_duplicatas(lista):
    nova_lista = []
    for numero in lista:
        encontrado = False
        for item in nova_lista:
            if item == numero:
                encontrado = True
                break
        if not encontrado:
            nova_lista.append(numero)
    
    lista.clear()
    for item in nova_lista:
        lista.append(item)

lista = popular_lista(10)

print("lista normal:")
exibir_lista(lista)

remover_duplicatas(lista)

print("lista sem duplicatas:")
exibir_lista(lista)
