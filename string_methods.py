def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = " Grace Hopper "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    var= "true"
    nya = "false"



    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")
    print(f"Find: {frase.find("gran")}")
    print(f"Replace: {frase.replace("programacion", "desarrollo")}")
    print(f"Count: {frase.count("a")}")
    if "Python" in frase:
        print(f"Contiene python: {var}")
    else:
        print(f"Contiene python: {nya}")

    if "java" in frase:
        print(f"Contiene java: {var}")
    else:
        print(f"Contiene java: {nya}")

    print(f"Slice: {frase[0:6]}")
    print(f"Paso: {frase[0:6:2]}")
    print(f"Inverso: {frase[6::-1]}")
    print(f"Formato:{nombre}sabe {frase[0:6]}")
    print("""
linea 1
linea 2
linea 3
    """)

string_methods()
