#ARCHIVOS (LEER)
archivo = open("datos.txt", "r") #r de read, para indicar que se va a leer datos.txt
contenido = archivo.read()  #para leer el archivo
print(contenido)
archivo.close() #cerrar una vez hemos concluido

#ARCHIVOS (CREAR)
archivo = open("datos.txt", "w") #w de write, para indicar que se va a escribir
archivo.write("Hola, mundo!")
archivo.close()

# with para AUTOMATIZAR
with open("datos.txt", "r") as archivo:
    contenido = contenido.read()
    print(contenido)