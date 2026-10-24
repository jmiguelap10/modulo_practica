import pytest
from modelos.inventario import Inventario
from modelos.producto import Producto
from modelos.producto_perecedero import ProductoPerecedero
from modelos.producto_digital import ProductoDigital
from persistencia.almacenamiento import AlmacenamientoJSON


def test_guardar_y_cargar_inventario(tmp_path):
    ruta_temporal = tmp_path / "test_inventario.json"
    almacenamiento = AlmacenamientoJSON(str(ruta_temporal))

    # 1. Crear inventario original con diferentes tipos
    inv_original = Inventario()
    inv_original.agregar_producto(Producto("Teclado", 150000.0, 10))
    inv_original.agregar_producto(ProductoPerecedero("Yogurt", 4000.0, 6, 2))
    inv_original.agregar_producto(ProductoDigital("Curso SQL", 90000.0, "https://cursos.dev/sql"))

    # 2. Guardar en disco temporal
    almacenamiento.guardar(inv_original)
    assert ruta_temporal.exists()

    # 3. Cargar en un inventario nuevo
    inv_recuperado = almacenamiento.cargar()

    # 4. Verificar integridad de datos y tipos
    assert len(inv_recuperado.productos) == 3

    teclado = inv_recuperado.buscar_producto("Teclado")
    assert type(teclado) is Producto
    assert teclado.stock == 10

    yogurt = inv_recuperado.buscar_producto("Yogurt")
    assert type(yogurt) is ProductoPerecedero
    assert yogurt.dias_para_caducar == 2

    curso = inv_recuperado.buscar_producto("Curso SQL")
    assert type(curso) is ProductoDigital
    assert curso.enlace_descarga == "https://cursos.dev/sql"


def test_cargar_archivo_inexistente_retorna_inventario_vacio(tmp_path):
    ruta_inexistente = tmp_path / "no_existe.json"
    almacenamiento = AlmacenamientoJSON(str(ruta_inexistente))

    inv = almacenamiento.cargar()
    assert len(inv.productos) == 0