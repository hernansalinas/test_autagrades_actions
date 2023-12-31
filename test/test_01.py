import pytest
#from actividad_01 import doble_factorial
import sys
sys.path.append('Students/Salinas_431')
from actividad_01 import doble_factorial

#from actividad_01 import doble_factorial

@pytest.mark.parametrize("n, resultado", [(5, 15), (6, 48), (7, 105), (8, 384)])
def test_doble_factorial(n, resultado):
    assert doble_factorial(n) == resultado
