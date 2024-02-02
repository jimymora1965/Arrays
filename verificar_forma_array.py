import numpy as np

array_aleatorio = np.random.rand(2, 3, 4)

# Imprimir el array
print(array_aleatorio)

# Verificar la dimensionalidad
if array_aleatorio.ndim == 3:
    print("El array es tridimensional.")
    print("Forma del array:", array_aleatorio.shape)
else:
    print("El array no es tridimensional.")
