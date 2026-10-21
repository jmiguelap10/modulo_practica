import pytest
from servicios.finanzas import calcular_iva

def test_calcular_iva_estandar():
    resultado = calcular_iva(100000)
    assert resultado == 19000.0
    
def test_calcular_iva_Cero():
    resultado = calcular_iva(0)
    #assert significa asegurar o afirmar 
    assert resultado == 0.0
    
def test_calcular_iva_monto_negativo():
    with pytest.raises(ValueError):
        calcular_iva(-50000)