#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60).
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação:
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

glicemia_do_momento = int(input('digite a glicemia do momento'))

meta_pre_refeicao = int(input('meta pré-refeição'))

fator_sensibilidade = int(input('meta pré-refeição'))

quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

print('quantidade_insulina')

#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

distancia = int(input('digite a distância a ser percorrida'))

tempo = int(input('digite o tempo desejado da viagem'))

velocidade_media = distancia / tempo

print(velocidade_media)

#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

distancia = int(input('digite a distância a ser percorrida'))

tempo = int(input('digite o tempo desejado da viagem'))

velocidade_media = distancia / tempo
tempo_viagem = distancia / velocidade_media

print(tempo_viagem)

#4 - O volume de um cubo é determinado através do produto da área da base pela altura,
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

altura = int(input('digite a altura da piscina'))

largura = int(input('digite a largura da piscina'))

comprimeto = int(input('digite o comprimento da piscina'))

volume = altura * largura * comprimeto

print(volume)

#5 - Faça um programa em linguagem Python que converta metros para centímetros.
metros = int(input('digite a medida em metros'))

centimetros = metros * 100

print(centimetros)

#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens:
#    Carioca Paulista Mineiro Outros estados

sigla = input('digite a sigla do seu estado').upper()

if sigla == 'RJ':
    print('Carioca')
elif sigla == 'SP':
    print('Paulista')
elif sigla == 'MG':
    print('Mineiro')
else:
    print('Outros estados')

#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)

nota1 = int(input('digite a primeira nota'))

nota2 = int(input('digite a segunda nota'))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('Aprovado')

elif media <= 3.0:
    print('Reprovado')

else:
    print('Exame')

#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.

listaDadosOriginais = []

while True:
    glicemia = int(input('digite o valor da glicemia'))
    listaDadosOriginais.append(glicemia)
    if glicemia == 0:
        break

print(listaDadosOriginais)

#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da listaDadosOriginais, um abaixo do outro.

listaDadosOriginais = []

while True:
    glicemia = int(input('digite o valor da glicemia'))
    listaDadosOriginais.append(glicemia)
    if glicemia == 0:
        break

for glicemia in listaDadosOriginais:
    print(glicemia)

#10 - Faça um complemento no código anterior para copiar a listaDadosOriginais para a
#     listaDadosOrdenados, que na sequência precisa ser ordenada.

listaDadosOriginais = []

while True:
    glicemia = int(input('digite o valor da glicemia'))
    listaDadosOriginais.append(glicemia)
    if glicemia == 0:
        break

    listaDadosOrdenados = listaDadosOriginais.copy()
    listaDadosOrdenados.sort()
    print(listaDadosOrdenados)

#11 - Faça um complemento no código anterior para mostrar o menor e o maior valores
#     de glicemia cadastrados.

listaDadosOriginais = []

while True:
    glicemia = int(input('digite o valor da glicemia'))
    listaDadosOriginais.append(glicemia)
    if glicemia == 0:
        break

    listaDadosOrdenados = listaDadosOriginais.copy()

    menor_valor = min(listaDadosOrdenados)
    maior_valor = max(listaDadosOrdenados)
    print("Menor valor:", menor_valor)
    print("Maior valor:", maior_valor)

#12 - Faça um complemento no código anterior para mostrar a média dos valores de
#     glicemia cadastros e na sequência contar e mostrar quantos valores estão abaixo e
#     acima da média.

listaDadosOriginais = []

while True:
    glicemia = int(input('digite o valor da glicemia'))
    listaDadosOriginais.append(glicemia)
    if glicemia == 0:
        break

# Remove the sentinel value (0) if it's not a valid glycemia reading
if 0 in listaDadosOriginais:
    listaDadosOriginais.remove(0)

listaDadosOrdenados = listaDadosOriginais.copy()
listaDadosOrdenados.sort()
print("Lista Ordenada: ", listaDadosOrdenados)

if listaDadosOriginais:
    media = sum(listaDadosOriginais) / len(listaDadosOriginais)
    print("Média dos valores de glicemia:", media)

    abaixo_media = 0
    acima_media = 0

    for valor in listaDadosOriginais:
        if valor < media:
            abaixo_media += 1
        elif valor > media:
            acima_media += 1

    print("Valores abaixo da média:", abaixo_media)
    print("Valores acima da média:", acima_media)
else:
    print("Nenhum valor de glicemia válido foi inserido.")
