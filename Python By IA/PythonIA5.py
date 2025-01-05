archivo = open("notas.txt", "w")
archivo.write("""Aprender Python es divertido. 
Hoy aprendí a manejar archivos.""")
archivo.close()

archivo = open("notas.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

with open("notas.txt", "a") as archivo:
    archivo.write("Manejo de archivos completado.\n")

archivo = open("notas.txt", "r")
for linea in archivo:
    print(linea.strip()) 
archivo.close()







