try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = num1 / num2 
except ValueError:
    print("Error: Debes introducir un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del programa.")


    






