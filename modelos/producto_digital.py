from modelos.producto import Producto

class ProductoDigital(Producto):
    def __init__(self, nombre: str, precio: float, enlace_descarga: str) -> None:
        # Los productos digitales tienen stock ilimitado; pasamos 1 como valor base
        super().__init__(nombre, precio, stock=1)
        self.enlace_descarga = enlace_descarga

    @property
    def enlace_descarga(self) -> str:
        return self._enlace_descarga

    @enlace_descarga.setter
    def enlace_descarga(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("El enlace de descarga debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("El enlace de descarga no puede estar vacío.")
        self._enlace_descarga = valor.strip()

    def reducir_stock(self, cantidad: int) -> None:
        """Polimorfismo: un producto digital nunca agota sus existencias."""
        pass
    
    def to_dict(self) -> dict:
            datos = super().to_dict()
            datos["tipo"] = "ProductoDigital"
            datos["enlace_descarga"] = self.enlace_descarga
            return datos
    