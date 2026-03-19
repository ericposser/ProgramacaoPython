hp_heroi = 100
hp_monstro = 100

while hp_heroi > 0 and hp_monstro > 0:    
    dano_heroi = float(input("dano do ataque do heroi: "))
    dano_monstro = float(input("dano do ataque do monstro: "))
    
    hp_monstro -= dano_heroi
    hp_heroi -= dano_monstro
    
    if hp_monstro < 0:
        hp_monstro = 0
    if hp_heroi < 0:
        hp_heroi = 0
    
    print(f"heroi:   {hp_heroi:.1f} HP")
    print(f"monstro: {hp_monstro:.1f} HP")

if hp_heroi > 0 and hp_monstro <= 0:
    print("heroi venceu")
elif hp_monstro > 0 and hp_heroi <= 0:
    print("monstro venceu")
else:
    print("empate")
