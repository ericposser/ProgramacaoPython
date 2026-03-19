capacidade = 15
peso_total = 0

while peso_total < capacidade:
    item = float(input("peso do item encontrado: "))
    
    if peso_total + item > capacidade:
        print("mochila cheia, item descartado")
        break
    
    peso_total += item
    print(f"item adicionado")

print(f"peso final na mochila: {peso_total:.1f}kg")
