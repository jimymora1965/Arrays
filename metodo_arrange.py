import numpy as np

# Ejemplo 1: Crear un array de 0 a 9
arr1 = np.arange(10)
print(arr1)
# Salida: [0 1 2 3 4 5 6 7 8 9]

# Ejemplo 2: Crear un array de 3 a 13 con paso 2
arr2 = np.arange(3, 14, 2)
print(arr2)
# Salida: [ 3  5  7  9 11 13]

# Ejemplo 3: Crear un array de 0 a 1 con paso 0.2 y tipo de datos float
arr3 = np.arange(0, 1.1, 0.2, dtype=float)
print(arr3)
# Salida: [0.  0.2 0.4 0.6 0.8 1. ]
