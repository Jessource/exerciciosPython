#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#print(json.dumps(contatos, indent=4))

arquivo = open ("C:\\Users\\LENOVO\Documents\\dicionario.json", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)
arquivo.close()
