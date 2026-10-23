class ProductoNoEncontradoError(Exception):
    """Excepción lanzada cuando un producto no existe en el inventario."""
    pass

class StockInsuficienteError(Exception):
    pass
