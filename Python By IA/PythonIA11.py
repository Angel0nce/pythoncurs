# Comprensión de Lista
divisibles_por_tres = [n for n in range(1, 21) if n % 3 == 0]
print("Divisibles por 3:", divisibles_por_tres)

# Comprensión de Diccionario
cubos = {n: n**3 for n in range(1, 6)}
print("Cubos:", cubos)

# Comprensión de Conjunto
numeros = [1, 2, 2, 3, 4, 4, 5]
cuadrados_unicos = {n**2 for n in numeros}
print("Cuadrados únicos:", cuadrados_unicos)
