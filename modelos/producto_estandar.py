from modelos.producto import Producto
from modelos.excepciones import StockInsuficienteError


class ProductoEstandar(Producto):
    def reducir_stock(self, cantidad: int) -> None:
        """Implementación concreta para productos físicos con stock limitado."""
        if cantidad > self.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para \"{self.nombre}\". "
                f"Disponible: {self.stock}, solicitado: {cantidad}."
            )
        self.stock -= cantidad

    def to_dict(self) -> dict:
        """Serializa los atributos de un producto estándar."""
        return {
            "tipo": "ProductoEstandar",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }