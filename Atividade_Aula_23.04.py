def ler_arquivo(caminho):
    with open(caminho) as arquivo:
        conteudo = arquivo.read()
    return conteudo

def preparar_lista_palavras(conteudo):
    lista_palavras = conteudo.splitlines()
    lista_palavras.sort()
    return lista_palavras

def obter_texto_usuario():
    txt = input('digite um texto para analise: ')
    lista_txt = txt.split(' ')
    return lista_txt

def contar_ocorrencias(lista_palavras, lista_txt):
    for palavra_negativa in lista_palavras:
        ocorrencias = 0
        for palavra_txt in lista_txt:
            if palavra_negativa == palavra_txt:
                ocorrencias += 1
        if ocorrencias > 0:
            print(f'ocorrencias da palavra {palavra_negativa} = {ocorrencias}')

caminho_arquivo = '/content/palavras.csv'
    
conteudo = ler_arquivo(caminho_arquivo)
lista_palavras = preparar_lista_palavras(conteudo)
lista_txt = obter_texto_usuario()
contar_ocorrencias(lista_palavras, lista_txt)
