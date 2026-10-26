from modelos.producto_estandar import ProductoEstandar


class ProductoPerecedero(ProductoEstandar):
    def __init__(self, nombre: str, precio: float, stock: int, dias_para_caducar: int) -> None:
        super().__init__(nombre, precio, stock)
        self.dias_para_caducar = dias_para_caducar

    @property
    def dias_para_caducar(self) -> int:
        return self._dias_para_caducar

    @dias_para_caducar.setter
    def dias_para_caducar(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("Los días para caducar deben ser un número entero.")
        if valor < 0:
            raise ValueError("Los días para caducar no pueden ser negativos.")
        self._dias_para_caducar = valor

    def calcular_precio_liquidado(self, porcentaje_descuento: float = 20.0) -> float:
        """Si quedan 3 días o menos para caducar, aplica un descuento especial."""
        if self._dias_para_caducar <= 3:
            return round(self.precio * (1 - porcentaje_descuento / 100), 2)
        return self.precio

    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos["tipo"] = "ProductoPerecedero"
        datos["dias_para_caducar"] = self.dias_para_caducar
        return datos