arquivo = "partida.txt"
kda_destaque = 2.0


def ler_partida(caminho):
    jogadores = []

    with open(caminho, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            dados = linha.split(";")

            jogador = {
                "nome":   dados[0],
                "classe": dados[1],
                "kills":  int(dados[2]),
                "deaths": int(dados[3]),
                "dano":   int(dados[4]),
            }
            jogadores.append(jogador)

    return jogadores


def calcular_kda(kills, deaths):
    if deaths == 0:
        return float(kills)
    return kills / deaths


def filtrar_por_classe(jogadores, classe):
    resultado = []
    for j in jogadores:
        if j["classe"].lower() == classe.strip().lower():
            resultado.append(j)
    return resultado


def maior_dano(jogadores):
    campeao = jogadores[0]
    for j in jogadores:
        if j["dano"] > campeao["dano"]:
            campeao = j
    return campeao


def media_kills(jogadores):
    total = sum(j["kills"] for j in jogadores)
    return total / len(jogadores)


def jogadores_kda_alto(jogadores, minimo=kda_destaque):
    resultado = []
    for j in jogadores:
        if calcular_kda(j["kills"], j["deaths"]) > minimo:
            resultado.append(j["nome"].upper())
    return resultado


def ordenar_por_dano(jogadores):
    for i in range(len(jogadores)):
        for k in range(i + 1, len(jogadores)):
            if jogadores[k]["dano"] > jogadores[i]["dano"]:
                jogadores[i], jogadores[k] = jogadores[k], jogadores[i]
    return jogadores


def imprimir_relatorio(jogadores):
    separador = "-" * 52

    print(f"\n{'JOGADOR':<14} {'CLASSE':<12} {'K':>4} {'D':>4} {'DANO':>7} {'KDA':>6}")
    print(separador)

    for j in jogadores:
        kda = calcular_kda(j["kills"], j["deaths"])
        print(
            f"{j['nome']:<14} {j['classe']:<12} "
            f"{j['kills']:>4} {j['deaths']:>4} "
            f"{j['dano']:>7} {kda:>6.2f}"
        )

    print(separador)
    print("DESTAQUES")

    campeao = maior_dano(jogadores)
    print(f"\nMaior dano causado : {campeao['nome']} ({campeao['dano']:,} de dano)")

    media = media_kills(jogadores)
    print(f"Media de kills     : {media:.1f} kills por jogador")

    destaques = jogadores_kda_alto(jogadores)
    if destaques:
        print(f"\nKDA superior a {kda_destaque}:")
        for nome in destaques:
            print(f"   {nome}")
    else:
        print(f"\nNenhum jogador com KDA acima de {kda_destaque}.")

    print("RANKING DOS MAGOS")
    print(separador)

    magos = filtrar_por_classe(jogadores, "Mago")
    if magos:
        magos_ordenados = ordenar_por_dano(magos)
        for pos, m in enumerate(magos_ordenados, start=1):
            print(f"  {pos}. {m['nome']:<12} {m['dano']:,} de dano")
    else:
        print("  Nenhum mago encontrado na partida.")



jogadores = ler_partida(arquivo)
imprimir_relatorio(jogadores)
