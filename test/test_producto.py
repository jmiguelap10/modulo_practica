import pytest
from modelos.producto import Producto

def test_creacion_producto_valido():
    p = Producto("Teclado Mecánico", 150000.0, 10)
    assert p.nombre == "Teclado Mecánico"
    assert p.precio == 150000.0
    assert p.stock == 10
    
def test_aplicar_descuento_valido():
    p = Producto("Mouse", 100000.0, 5)
    p.aplicar_descuento(10)
    assert p.precio == 90000.0
    
def test_error_precio_negativo():
    with pytest.raises(ValueError, match="El precio debe ser mayor a cero."):
        Producto("Mouse", -500.0, 5)
        
def test_error_nombre_vacio():
    with pytest.raises(ValueError, match="El nombre del producto no puede estar vacio."):
        Producto(" ", 1000.0, 5)
        
def test_error_descuento_fuera_de_rango():
    p = Producto("Monitor", 500000.0, 2)
    with pytest.raises(ValueError, match="El porcentaje de descuento debe estar entre 0 y 100."):
        p.aplicar_descuento(150)
        