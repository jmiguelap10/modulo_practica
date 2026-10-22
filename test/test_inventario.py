import pytest
from modelos.producto import Producto
from modelos.inventario import Inventario

def test_inventario_vacio():
    inv = Inventario()
    assert len(inv.productos) == 0
    assert inv.total_unidades() == 0
    assert inv.valor_total_inventario() == 0.0
    
def test_agregar_productos_y_calcular_totales():
    inv = Inventario()
    p1 = Producto("Teclado", 100000.0, 2)
    p2 = Producto("Mouse", 50000.0, 3)
    
    inv.agregar_producto(p1)
    inv.agregar_producto(p2)
    
    assert len(inv.productos) == 2
    assert inv.total_unidades() == 5
    assert inv.valor_total_inventario() == 350000.0
    
def test_error_agregar_tipo_invalido():
    inv = Inventario()
    with pytest.raises(TypeError, match="Solo se puede agregar instancias de la clase Producto."):
        inv.agregar_producto("Un texto cualquiera.")
    