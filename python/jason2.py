import json
arquivo = open ("C:\\Users\\LENOVO\Documents\\dicionario.json", "r", encoding="UTF-8")
conteudo = arquivo.read()
arquivo.close()
agenda = json.loads(conteudo)
print(agenda)

