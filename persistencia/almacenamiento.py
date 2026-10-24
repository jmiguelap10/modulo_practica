import json
from pathlib import Path
from modelos.inventario import Inventario
from modelos.producto import Producto
from modelos.producto_perecedero import ProductoPerecedero
from modelos.producto_digital import ProductoDigital


def fabricar_producto_desde_dict(datos: dict) -> Producto:
    """Reconstruye la instancia adecuada según el tipo serializado."""
    tipo = datos.get("tipo")
    nombre = datos["nombre"]
    precio = datos["precio"]

    if tipo == "Producto":
        return Producto(nombre, precio, datos["stock"])
    elif tipo == "ProductoPerecedero":
        return ProductoPerecedero(nombre, precio, datos["stock"], datos["dias_para_caducar"])
    elif tipo == "ProductoDigital":
        return ProductoDigital(nombre, precio, datos["enlace_descarga"])
    else:
        raise ValueError(f"Tipo de producto desconocido: {tipo}")


class AlmacenamientoJSON:
    def __init__(self, ruta_archivo: str = "inventario.json") -> None:
        self.ruta = Path(ruta_archivo)

    def guardar(self, inventario: Inventario) -> None:
        """Guarda la lista de productos en un archivo JSON."""
        datos = [prod.to_dict() for prod in inventario.productos]
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar(self) -> Inventario:
        """Carga los productos desde el archivo JSON; si no existe, devuelve un inventario vacío."""
        inventario = Inventario()
        if not self.ruta.exists():
            return inventario

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for item in datos:
            producto = fabricar_producto_desde_dict(item)
            inventario.agregar_producto(producto)

        return inventario