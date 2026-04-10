def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("ingrese su nombre")
    apellido = input("ingrese su apellido")

    var = nombre+" "+apellido
    print(var.lower())
    print(var.title())
    print(var.upper())
    print("\t" + var.lower())








