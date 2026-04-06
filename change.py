def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingrese el gasto"))
    dinerorecibido = int(input("Ingrese el dinero"))

    vuelto = dinerorecibido - gasto

    pesos = int(vuelto)

    centavos = int((vuelto - pesos)*100)

    print("\nvuelto\n")
    print(f"pesos: \n{pesos}")
    print(f"centavos: \n{centavos}")

