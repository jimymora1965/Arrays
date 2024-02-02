import numpy as np

# Crear dos arrays de diferentes tamaños
array1 = np.array([[1, 2, 3], [4, 5, 6]])  # Forma (2, 3)
array2 = np.array([10, 20, 30])              # Forma (3,)

# Sumar los dos arrays (broadcasting)
resultado = array1 + array2

# Mostrar el resultado
print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
print("\nResultado de la suma:")
print(resultado)
