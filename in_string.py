def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingrese nombre: ").lower()


    var = "True"
    nya = "False"



    if "a" in nombre:
        print(f"Contiene a: {var}")

    else:
        print(f"Contiene a: {nya}")

    if "e" in nombre:
        print(f"Contiene e: {var}")

    else:
        print(f"Contiene e: {nya}")

    if "i" in nombre:
        print(f"Contiene i: {var}")

    else:
        print(f"Contiene i: {nya}")

    if "o" in nombre:
        print(f"Contiene o: {var}")

    else:
        print(f"Contiene o: {nya}")

    if "u" in nombre:
        print(f"Contiene u: {var}")

    else:
        print(f"Contiene u: {nya}")




