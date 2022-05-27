
dicionario = { 

    "1": "um",
    "2": "dois",
    "3": "tres"
}
#printa os valores
#print (dicionario.values())

#for valor in dicionario.values():
 #   print(valor)

#printa as chaves

#print(dicionario.keys())

#for chave in dicionario.keys():
#    print(chave)


#printando um valor de uma determinada chave
#print(dicionario["1"])

#printando chaves e valores junto

for chave1, valor2 in dicionario.items():
    print("{} - {}".format(chave1,valor2))
