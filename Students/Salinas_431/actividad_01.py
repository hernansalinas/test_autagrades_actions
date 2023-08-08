#!/usr/bin/env python
## Definir la función que calcula el doble factorial
def doble_factorial(n):
  # Verificar que n sea un número entero positivo
  if not isinstance(n, int) or n < 0:
    raise ValueError("n debe ser un número entero positivo")
  # Inicializar el resultado con el valor de n
  resultado = n
  # Usar un bucle while para ir multiplicando los números con la misma paridad que n
  while n > 1:
    # Restar dos unidades a n
    n -= 2
    # Multiplicar el resultado por n
    resultado *= n
  # Devolver el resultado
  return resultado

