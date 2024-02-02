import numpy as np

# Crear un array bidimensional (matriz) de forma 3x3
array_bidimensional = np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])

# Imprimir la matriz
print("Matriz bidimensional:")
print(array_bidimensional)

# Acceder a elementos individuales por índices
elemento_central = array_bidimensional[1, 1]
primer_fila = array_bidimensional[0, :]
tercera_columna = array_bidimensional[:, 2]

# Imprimir elementos individuales o porciones
print("\nElemento central:", elemento_central)
print("Primer fila:", primer_fila)
print("Tercera columna:", tercera_columna)
