from modelos.producto import Producto

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
    