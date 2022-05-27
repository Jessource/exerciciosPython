def validar_categoria(categoria_usuario):
    if categoria_usuario.upper() in categorias:
        print("categoria válida")
    else:
        print("categoria inválida")

categorias = ["A","B", "C", "D", "E"]

