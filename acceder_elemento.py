#accede al tercer elementos de las dos primeras filas de un array
import numpy as np

# Crear un array bidimensional (matriz) de forma 3x3
array_bidimensional = np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])

# Imprimir la matriz
print("Matriz bidimensional:")
print(array_bidimensional)

# Acceder al tercer elemento de las dos primeras filas
tercer_elemento_primera_fila = array_bidimensional[0, 2]
tercer_elemento_segunda_fila = array_bidimensional[1, 2]

# Imprimir los resultados
print("\nTercer elemento de la primera fila:", tercer_elemento_primera_fila)
print("Tercer elemento de la segunda fila:", tercer_elemento_segunda_fila)
