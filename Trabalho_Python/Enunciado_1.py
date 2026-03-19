meta = int(input("meta de biomassa (em unidades): "))

biomassa_total = 0
arvores = 0

while biomassa_total < meta:
    biomassa = int(input(f"arvore {arvores + 1} - digite o valor de biomassa: "))
    biomassa_total += biomassa
    arvores += 1

print("meta atingida!")
print(f"arvores plantadas: {arvores}")
