contatos = {
    "Clark Kent":{
        "celular": "123456",
        "email":"mhmj@gmail.com"
    },
    "Brunce Wayne":{
        "celular": "6789",
         "email":"beta@gmail.com"
    }
}




for contatos, formas in contatos.items():
    for celular, email in formas.items():
        print("O contato {} pode ser encontrado  {} :  {}".format(contatos, celular, email))
