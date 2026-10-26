import pytest
from modelos.producto import Producto
from modelos.producto_estandar import ProductoEstandar


def test_no_se_puede_instanciar_clase_abstracta():
    """Verifica que Producto actúe estrictamente como contrato abstracto."""
    with pytest.raises(TypeError, match="Can't instantiate abstract class Producto"):
        Producto("Genérico", 100.0, 5) #pylint: disable=abstract-class-instantiated

def test_producto_estandar_cumple_contrato():
    prod = ProductoEstandar("Mouse Óptico", 45000.0, 10)
    assert isinstance(prod, Producto)
    
    prod.reducir_stock(4)
    assert prod.stock == 6

    datos = prod.to_dict()
    assert datos["tipo"] == "ProductoEstandar"