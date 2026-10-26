import pytest
from modelos.producto_estandar import ProductoEstandar
from modelos.inventario import Inventario
from modelos.excepciones import ProductoNoEncontradoError, StockInsuficienteError
def test_inventario_vacio():
    inv = Inventario()
    assert len(inv.productos) == 0
    assert inv.total_unidades() == 0
    assert inv.valor_total_inventario() == 0.0
    
def test_agregar_productos_y_calcular_totales():
    inv = Inventario()
    p1 = ProductoEstandar("Teclado", 100000.0, 2)
    p2 = ProductoEstandar("Mouse", 50000.0, 3)
    
    inv.agregar_producto(p1)
    inv.agregar_producto(p2)
    
    assert len(inv.productos) == 2
    assert inv.total_unidades() == 5
    assert inv.valor_total_inventario() == 350000.0
    
def test_error_agregar_tipo_invalido():
    inv = Inventario()
    with pytest.raises(TypeError, match="Solo se puede agregar instancias de la clase Producto."):
        inv.agregar_producto("Un texto cualquiera.")
        
def test_buscar_producto_existente():
    inv = Inventario()
    teclado = ProductoEstandar("Teclado Mecánico", 150000.0, 5)
    inv.agregar_producto(teclado)
    
    encontrado = inv.buscar_producto("teclado mecánico")
    assert encontrado == teclado
    assert encontrado.precio == 150000.0
    
def test_error_buscar_producto_inexistente():
    inv = Inventario()
    with pytest.raises(ProductoNoEncontradoError, match="El producto \"Mouse Gamer\" no existe en el inventario."):
        inv.buscar_producto("Mouse Gamer")
        
def tes_retirar_stock_exitoso():
    inv = Inventario()
    p = ProductoEstandar("Monitor", 800000.0, 10)
    inv.agregar_producto(p)
        
    inv.retirar_stock("Monitor", 3)
    assert p.stock == 7
        
def test_error_retirar_stock_insuficiente():
    inv = Inventario()
    p = ProductoEstandar("Monitor", 800000.0, 5)
    inv.agregar_producto(p)
    
    with pytest.raises(StockInsuficienteError, match="Stock insuficiente para \"Monitor\". Disponible: 5, solicitado: 8."):
        inv.retirar_stock("Monitor", 8)
        
def test_error_retirar_cantidad_invalida():
    inv = Inventario()
    p = ProductoEstandar("Monitor", 800000, 5)
    inv.agregar_producto(p)
    
    with pytest.raises(ValueError, match="La cantidad a retirar debe ser mayor a cero."):
        inv.retirar_stock("Monitor", 0)
    