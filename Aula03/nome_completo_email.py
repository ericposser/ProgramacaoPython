while(True):
  nome_completo = input("digite seu nome completo: ")
  palavras_nome = nome_completo.split()
  if(len(palavras_nome) >= 2):
    print("seu nome completo e: ", nome_completo)
    print("seu nom eh: ", palavras_nome[0])
    print("seu sobrenome eh: ", palavras_nome[-1])
    
    primeiro_nome = palavras_nome[0].lower()
    ultimo_nome = palavras_nome[-1].lower()
    email = primeiro_nome + "." + ultimo_nome + "@ufn.edu.br"
    print("seu email eh: ", email)
    break

  print("nome invalido")
