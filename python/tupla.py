categorias = ("baba", "bobo", "bubu", "babao")
print(categorias)
print(categorias[-1])

for categoria in categorias:
    print(categoria)

#contagem de elementos
tupla = (1,7,7,19,3,2,11,15,6,1,5)
contagem = tupla.count(7)
print (f"nessa tupla o numero {7} aparece {contagem} vezes")

#indice em que encontrou o valor
indice = tupla.index(11)
print(f"o numero {11} foi encontrado no indice: {indice}")
