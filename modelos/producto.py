from modelos.excepciones import StockInsuficienteError

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        
        self.nombre = nombre.strip()
        self.precio = precio
        self.stock = stock
        
    @property
    def precio(self) -> float:
        """Getter: se ejecuta cuando alguien lee p.precio"""
        return self._precio
        
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        """Setter: se ejecuta cuando alguien intenta hacer p.precio = nuevo_precio"""
        nuevo_precio = float(nuevo_precio)
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = nuevo_precio
        
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, nuevo_stock: int) -> None:
        nuevo_stock = int(nuevo_stock)
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = nuevo_stock
        
    def aplicar_descuento(self, porcentaje: float) -> None:
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        
    def reducir_stock(self, cantidad: int) -> None:
        """Disminuye el stock físico si hay unidades suficientes."""
        if cantidad > self.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para \"{self.nombre}\". "
                f"Disponible: {self.stock}, solicitado: {cantidad}."
            )
        self.stock -= cantidad
        
    def to_dict(self) -> dict:
        """Serializa los atributos base del producto a un diccionario."""
        return {
            "tipo": "Producto",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }
        