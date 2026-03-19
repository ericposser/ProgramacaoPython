while True:
    nivel = float(input("nivel do rio (valor negativo para encerrar): "))
    
    if nivel < 0:
        print("encerrando monitoramento.")
        break
    elif nivel < 3:
        print("estado normal")
    elif nivel <= 5:
        print("estado de alerta")
    else:
        print("evacuacao imediata")
