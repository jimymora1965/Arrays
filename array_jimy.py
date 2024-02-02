import numpy as np

miarray = np.array([1,2,3,4,5])
print()
print("Mi Array en rango 0 al 27:\n",miarray)

#crear un array con rango 0 al 27

print("\nCreando array unidimensional con rango 0 al 27:")
mi_array = np.arange(28)
print(mi_array)

#modificar un elemento de mi array

print("\nCodigo para modificar un valor del array")

# Crear un array unidimensional con valores del 0 al 5
array_unidimensional = np.arange(6)

# Imprimir el array original
print("Array unidimensional original:", array_unidimensional)

# Modificar el cuarto elemento (índice 3) del array
nuevo_valor = 100
array_unidimensional[3] = nuevo_valor

# Imprimir el array modificado
print("Array unidimensional modificado:", array_unidimensional)
