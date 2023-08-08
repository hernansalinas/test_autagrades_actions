#!/usr/bin/env python
## Definir la función que calcula el doble factorial
def doble_factorial(n):
    # Verificar que n sea un entero positivo
    if not isinstance(n, int) or n < 0:
        return None
    # Inicializar el acumulador con 1
    resultado = 1
    # Iterar mientras n sea mayor o igual a 1
    while n >= 1:
        # Multiplicar el acumulador por n
        resultado = resultado * n
        # Restar 2 a n
        n = n - 2
    # Devolver el acumulador
    return resultado

