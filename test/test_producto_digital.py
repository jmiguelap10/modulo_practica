import pytest
from modelos.producto_digital import ProductoDigital
from modelos.inventario import Inventario

def test_creacion_producto_digital_valido():
    curso = ProductoDigital("Curso Python Profesional", 120000.0, "https://cursos.dev/python")
    assert curso.nombre == "Curso Python Profesional"
    assert curso.precio == 120000.0
    assert curso.enlace_descarga == "https://cursos.dev/python"

def test_error_enlace_descarga_invalido():
    with pytest.raises(ValueError, match="El enlace de descarga no puede estar vacío."):
        ProductoDigital("Ebook", 35000.0, "   ")

def test_stock_no_disminuye_al_retirar_en_inventario():
    inv = Inventario()
    ebook = ProductoDigital("Guía de Patrones OOP", 45000.0, "https://descargas.dev/oop")
    inv.agregar_producto(ebook)

    # Retiramos 50 unidades y el método no debe lanzar StockInsuficienteError
    inv.retirar_stock("Guía de Patrones OOP", 50)
    assert ebook.stock == 1