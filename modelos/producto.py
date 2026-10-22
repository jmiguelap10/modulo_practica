class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.stock = int(stock)
        
    def aplicar_descuento(self, porcentaje: float) -> None:
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        