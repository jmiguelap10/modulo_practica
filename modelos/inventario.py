from modelos.producto import Producto
from modelos.excepciones import StockInsuficienteError
from modelos.excepciones import ProductoNoEncontradoError

class Inventario:
    def __init__(self) -> None:
        #Inicializamos una lista vacia para almacenar los productos
        self.productos: list[Producto] = []
        
    def agregar_producto(self, producto: Producto) -> None:
        #Validación: verificamos que el objeto sea una instancia real de Producto
        if not isinstance(producto, Producto):
            raise TypeError("Solo se puede agregar instancias de la clase Producto.")
        
        self.productos.append(producto)
        
    def total_unidades(self) -> int:
        """Calcula la suma del stock de todos los productos en el inventario."""
        return sum(p.stock for p in self.productos)
    
    def valor_total_inventario(self) -> float:
        """Calcula el valor monetario total multiplicando precio * stock de cada producto."""
        return sum(p.precio * p.stock for p in self.productos)
    
    def buscar_producto(self, nombre: str) -> Producto:
        """Busca un producto por nombre (sin distinguir mayúculas ni espacios extras)."""
        nombre_normalizado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_normalizado:
                return producto
            
        raise ProductoNoEncontradoError(F"El producto \"{nombre.strip()}\" no existe en el inventario.")
    
    def retirar_stock(self, nombre: str, cantidad: int) -> None:
        """Reduce la cantidad de stock de un producto si hay existencia suficientes."""
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a cero.")
        
        producto = self.buscar_producto(nombre)
        
        if cantidad > producto.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para \"{producto.nombre}\". "
                f"Disponible: {producto.stock}, solicitado: {cantidad}."
            )
        
        producto.stock -=cantidad
        