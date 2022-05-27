tupla = (1,7,7,19,3,2,11,15,6,1,5)
print (f" a tupla foi criada assim:{tupla}")

#utilizando enumerate para mostrar uma sequencia
for numero, valor in enumerate(tupla):
    print (f"no indice {numero} temos: {valor}")

#mostrando a quantidade de itens na tupla
print(f"quantidade: {len(tupla)}")

#mostrando o valor minimo na tupla
print (f"minimo: {min(tupla)}")

#mostrando o valor maximo na tupla
print (f"maximo: {max(tupla)}")

#mostrando a soma de todos os valores da tupla
print (f"maximo:{sum(tupla)}")

#utilizando tuple() para a conversao de umaa lista para tupla

lista= [True, True]
print(f"Lista:{lista}")
tupla2 = tuple(lista)
print(f"Tupla:{tupla2}")


#criando a tupla3 com os valores 1 (True) e 0 (false)
tupla3 =(1,1)
#função all
print(f"testando a tupla2 com all:{all(tupla2)}")
print(f"testando a tupla3 com all:{all(tupla3)}")


#função any: retorna false se todos os valores forem false
print(f"testando a tupla2 com all:{all(tupla2)}")
print(f"testando a tupla3 com all:{all(tupla3)}")
