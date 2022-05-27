dicionario = { 

    "1": "um",
    "2": "dois",
    "3": "tres"
}

for chave1, valor2 in dicionario.items():
    print("{} - {}".format(chave1,valor2))

#inserido novas chaves e valores no dicionario

nova_chave = input ("Informe o nome da chave")
novo_valor = input ("Informe o valor da chave")

dicionario[nova_chave] = novo_valor
for chave1, valor2 in dicionario.items():
    print("{} - {}".format(chave1,valor2))
