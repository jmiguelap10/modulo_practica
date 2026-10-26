from abc import ABC, abstractmethod
from modelos.excepciones import StockInsuficienteError


class Producto(ABC):
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError("El precio debe ser un número numérico.")
        if valor < 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("El stock debe ser un número entero.")
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def aplicar_descuento(self, porcentaje: float) -> None:
        """Aplica un descuento porcentual sobre el precio base."""
        if not isinstance(porcentaje, (int, float)) or isinstance(porcentaje, bool):
            raise TypeError("El porcentaje de descuento debe ser un valor numérico.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    @abstractmethod
    def reducir_stock(self, cantidad: int) -> None:
        """Contrato obligatorio: cada subclase define cómo reduce su existencias."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Contrato obligatorio: cada subclase define su serialización."""
        pass