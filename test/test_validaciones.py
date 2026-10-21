import pytest
from validaciones import es_mayor_de_edad

@pytest.mark.parametrize(
    "edad, esperado",
    [
        (17, False),
        (18, True),
        (25, True),
        (0, False),
        (100, True),
    ],
)

def test_es_mayor_edad(edad, esperado):
    assert es_mayor_de_edad(edad) is esperado
    
def test_es_mayor_edad_negativa():
    with pytest.raises(ValueError):
        es_mayor_de_edad(-5)