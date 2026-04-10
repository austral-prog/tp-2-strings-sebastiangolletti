def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)


    frase = "  FICHA DEl ALUMNO"
    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    nombre = input("ingrese su nombre y apellido: ").strip().title()

    print(f"Nombre: {nombre.title()}")
    espacio = nombre.find(" ")

    nombr = nombre[:espacio]
    apellido = nombre[espacio+ 1:]
    email = input("ingrese su email: ").lower()
    print(f"Email: {email}")
    cantidad = len(nombre)
    print(f"Caracteres en nombre: {cantidad}")

    print(f"Iniciales: {nombre[0].upper()}{nombre[espacio+1].upper()}")

    print(f"Usuario: {apellido.lower()}.{nombr.lower()}")

    T = "True"
    F = "False"

    if "@" in email:
        print(f"Email valido: {T}")
    else:
        print(f"Email valido: {F}")

    A = email.find("@")
    B = email[A + 1:]
    print(f"Dominio: {B.lower()}")


    print(f"Nombre para archivo: {nombre.replace(" ","_").title()}")

    print(f"Cantidad de a: {nombre.lower().count("a")}")

    print(f"Codigo secreto: {nombre[::-1].upper()}")

    nota1 = int(input("ingrese nota1: "))
    nota2 = int(input("ingrese nota2: "))
    nota3 = int(input("ingrese nota3: "))

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")

    print(f"Nota 3: {nota3}")


    print(f"Suma: {(nota1 + nota2 + nota3):.0f}")
    print(f"Promedio: {(nota1 + nota2 + nota3) / 3}")
    print(f"Promedio entero: {int((nota1 + nota2 + nota3) / 3)}")

    print("========================")








