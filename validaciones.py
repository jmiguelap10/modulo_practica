def es_mayor_de_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad >= 18

if __name__ == "__main__":
    print("Probando:", es_mayor_de_edad(20))