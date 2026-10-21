def calcular_iva(monto):
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    return monto * 0.19

if __name__ == "__main__":
    print(calcular_iva(10000))