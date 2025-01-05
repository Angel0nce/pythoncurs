print("Ingresa un numero positivo del 1 al 10")
Num = int(input("> "))

for i in range(1, 11):  # Itera del 1 al 10
    if i == Num:  # Si el número actual coincide con el ingresado
        print("¡Encontrado! Este es tu número.")
        break  # Detiene el bucle
    print(i)  # Imprime el número actual
 

    


