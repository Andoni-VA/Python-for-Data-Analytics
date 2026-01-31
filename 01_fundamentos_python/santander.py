
#FUNCIONES
def saludo(nombre,a,b):
    edad = a + b #variable local, sólo se puede usar en la función
    print("Hola, ",nombre,", tienes ",a+b," años")
saludo("Adrián",4,7)

#FUNCIONES LAMBDA (ANÓNIMAS)
cuadrado = lambda x: x**2 #función diminuta y rápida // lambda argumentos : expresión
print(cuadrado(5)) #imprime 25

#FUNCIONES CON NÚMERO VARIABLE DE ARGUMENTOS
def suma_variable(*numeros): #asterisco para avisar de que cantidad variable
    total = 0
    for numero in numeros:
        total = total + numero
    return total #el valor que devuelve la función


print(suma_variable(1,4,5,2)) #devuelve 12
