import pytest
from modelos.producto_perecedero import ProductoPerecedero
from modelos.inventario import Inventario

def test_creacion_producto_perecedero_valido():
    leche = ProductoPerecedero("Leche Entera", 4500.0, 20, 5)
    assert leche.nombre == "Leche Entera"
    assert leche.precio == 4500.0
    assert leche.stock == 20
    assert leche.dias_para_caducar == 5

def test_descuento_por_vencimiento_proximo():
    yogurt = ProductoPerecedero("Yogurt Griego", 10000.0, 10, 2)
    # Al quedar 2 días, aplica 20% de descuento por defecto -> 8000.0
    assert yogurt.calcular_precio_liquidado() == 8000.0

def test_sin_descuento_si_no_esta_proximo_a_vencer():
    queso = ProductoPerecedero("Queso Campesino", 12000.0, 8, 10)
    assert queso.calcular_precio_liquidado() == 12000.0

def test_error_dias_para_caducar_invalido():
    with pytest.raises(ValueError, match="Los días para caducar no pueden ser negativos."):
        ProductoPerecedero("Carne", 25000.0, 4, -1)

def test_inventario_acepta_producto_perecedero_polimorficamente():
    inv = Inventario()
    leche = ProductoPerecedero("Leche Entera", 4000.0, 5, 2)
    
    # Debe agregarse sin errores de tipo
    inv.agregar_producto(leche)
    
    assert inv.total_unidades() == 5
    assert inv.valor_total_inventario() == 20000.0
    assert inv.buscar_producto("leche entera") == leche