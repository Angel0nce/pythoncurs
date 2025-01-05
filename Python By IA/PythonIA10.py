def validar_entrada(func):
    def wrapper(n):
        if n < 0:
            print("El número debe ser positivo")
            return None
        return func(n)
    return wrapper

@validar_entrada
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial  # Mover el return fuera del bucle

# Entrada del usuario y cálculo
Numero = int(input("Ingrese un número: "))
resultado = calcular_factorial(Numero)
if resultado is not None:
    print(f"El factorial de {Numero} es {resultado}")







