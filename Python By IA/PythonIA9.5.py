print("Elije que opcion utilizar")
Opcion = int(input("""1- Convertir temperatura de Celcius a Fahrenheits.
2- Saber si un numero es par o impar.
> """))

if Opcion == 1:
    Temperatura = float(input("Introduce la temperatura a convertir: "))
    from PythonIA9 import convertir_celsius_a_fahrenheit
    print("La temperatura en Fahrenheit es:", convertir_celsius_a_fahrenheit(Temperatura))
elif Opcion == 2:
    Numero = int(input("Introduce el numero a evaluar: "))
    from PythonIA9 import es_par
    print("El numero es:", "par" if es_par(Numero) else "impar")




