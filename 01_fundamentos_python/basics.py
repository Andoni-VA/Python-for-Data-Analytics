#Empezando a utilizar Python para la ciencia de datos

nombre = "Andoni"            # string
apellidos = "Vázquez Arza"
carrera = "Física"
sueldo = 33_000.00           # float // ignora la barrabaja_
edad = 22                    # integer

mensaje = f"El empleado {nombre} tiene {edad} años" #string formatting

# help(str) te muestra el "manual" de las cadenas de texto

print(mensaje)

ap12 = apellidos.split(" ") # Crea una lista separando el string

print(ap12[1]) #imprime el segundo apellido, n=0,1,2,3...

ap12[0],ap12[1]=ap12[1],ap12[0]

print(ap12)