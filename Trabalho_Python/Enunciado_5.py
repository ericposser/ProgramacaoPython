dias = int(input("dias para analisar: "))

soma = 0
dia_atual = 1

while dia_atual <= dias:
    temp = float(input(f"temperatura do dia {dia_atual}: "))
    soma += temp
    dia_atual += 1

media = soma / dias

print(f"media de temperatura: {media:.1f}°C")

if media > 25:
    print("acima do esperado")
else:
    print("dentro da normalidade")
