dicionario = { 

    "1": "um",
    "2": "dois",
    "3": "tres"
}

for chave1, valor2 in dicionario.items():
    print("{} - {}".format(chave1,valor2))

dicionario["1"] = "meme"


for chave1, valor2 in dicionario.items():
    print("{} - {}".format(chave1,valor2))