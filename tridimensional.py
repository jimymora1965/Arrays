import numpy as np

# Crear un array tridimensional (3x3x3) lleno de ceros
array_tridimensional = np.zeros((3, 3, 3))

# Asignar algunos valores al array
for i in range(3):
    for j in range(3):
        for k in range(3):
            array_tridimensional[i, j, k] = i + j + k

# Imprimir el array tridimensional
print(array_tridimensional)

