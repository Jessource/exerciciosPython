import sys
#depois criamos algumas variáveis de exemplo

nome = "Bruce Wayne"
idade = 30
peso = 92.3

#vamos exibir em uma mensagem o nome da variavel, o tipo(type)
# e o tamanho(getsizeof)
print(" a variavel nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print(" a variavel idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print(" a variavel nome é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

#importando o módulo sys para conseguirmos usar o getsizeof
#criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()
#printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))