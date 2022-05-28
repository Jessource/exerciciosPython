arquivo = open ("C:\\Users\\LENOVO\Documents\\textoaleatorio.txt", encoding="UTF-8")


for linha in arquivo.readlines():
    print(linha)

arquivo.close()