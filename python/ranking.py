Descomplica = ["Descomplica","2021-03","endereços de e-mail","nomes", "dados parciais de cartão de crédito", "senhas", "compras"]
Dubsmash = ["Dubsmash","2018-12", "endereços de e-mail", "localizações geográficas", "nomes", "senhas", "números de telefone", "idiomas falados", "nomes de usuário"]
Gravatar = ["Gravatar","2020-10","endereços de e-mail","nomes", "nomes de usuário"]
Vakinha = ["Vakinha", "2020-06","datas de nascimento", "endereços de e-mail", "endereços IP", "nomes", "senhas", "números de telefone"]
Wattpad = ["Wattpad","2022-02","biografias", "datas de nascimento", "endereços de e-mail", "gêneros", "localizações geográficas", "endereços IP", "nomes", "senhas", "perfis de mídia social", "URLs de sites de usuários", "nomes de usuários"]

# criando uma lista RANKING para receber cada lista de empresa com os seus dados de vazamento
ranking = [Descomplica, Dubsmash, Gravatar, Vakinha, Wattpad]
# Exibindo a ordem inicial com o for
print("Ordem inicial: Empresas e seus vazamentos:")
for i in range(len(ranking)):
    print(f"{i + 1}) {ranking[i]}")
print("\n")

# Criando a função ordenarRanking que recebe por parâmetro as listas das empresas
# a função retorna por ordem de critérios de dados comprometidos como senha, ajuda da senha, número do telefone, nomes, e-mail e data do vazamento e utilizei a função "count"
# para verificar se o dado existe na lista.
def ordenarRanking(empresa):
    # Utilizei uma lógica de pesos.
    # Como o dado mais critico a ser vazado é a senha, coloquei o maior peso nela, 5 (cinco)
    # Ai fui diminuindo 1 em cada peso, e por padrão o peso é 0 (zero)
    peso = 0;
    if (empresa.count("senhas")):
        peso = 5
    elif (empresa.count("dicas de senha")):
        peso = 4
    elif (empresa.count("números de telefone")):
        peso = 3
    elif (empresa.count("nomes")):
        peso = 2
    elif (empresa.count("endereços de e-mail")):
        peso = 1
    # obs: Como elemento empresa[0] é "nome da empresa" e quero somente buscar a data de vazamento, então busco por empresa[1], onde fica a data de vazamento
    return (peso, empresa[1]) 

# A função sort por padrão ordena a lista por ordem crescente, porém não é o que queremos..
# Então utilizo função sort passando a propriedade reverse=True, que vai ordenar por ordem descrecente 
# e por ultimo chamamos a função "ordenarRanking" que irá ranquear as listas de empresas por ordem de critério de dados.
ranking.sort(reverse=True, key=ordenarRanking)
                                       
# Lista ordenada (ranking final)
print("Ordenação final")
for i in range(len(ranking)):
    print(f"{i + 1}) {ranking[i][0]}")
