def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese la cantidad : "))

    preciocondescuento = precio - descuento

    total = preciocondescuento * cantidad

    print(f"precio: {precio}")
    print(f"descuento: {descuento}")
    print(f"precio con descuento: {preciocondescuento}")
    print(f"total: {total}")





