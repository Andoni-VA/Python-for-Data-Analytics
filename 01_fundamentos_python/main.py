
#VARIABLES
altura = 1.65  #real
edad = 12      #int
casado = True  #Booleano
nombre = "Marcos" #string
frutas = ["Manzanas","Peras","Sandías"] #lista
 
#CONDICIONALES
if altura < 1.70 :
    print('Qué chaval más bajito') #Este es un comentario
    print('Come más ',frutas[0]) #o frutas[-3]
elif altura > 1.90 :
    print('Qué chaval más alto')
    print('Come menos ',frutas[1]) #o frutas[-2]
else:
    print('Medianos en mi jardín')
    print('Come un poco de ', frutas[2]) #o frutas[-1]

#BUCLES
contador = 0
while contador < 5:
    contador = contador + 1
    print(contador)

for i in range(edad):
    print('Tu edad ya no es ',i)

#LISTAS
frutas.append("Cerezas") #añado un elemendo al final
frutas.insert(1,"Uva") #se coloca en el elemento 1, desplaza el resto
frutas.remove("Manzanas") #elimina el elemento

fruta_eliminada = frutas.pop(2) #pop elimina y devuelve un elemento en una posic. espec.
frutas.sort() #imprime la lista
frutas.reverse() #imprime la lista al revés

numeros = [1,2,3,4,5,6]
cuadros = [x**2 for x in numeros if x % 2 == 0] #crea una nueva lista a partir de una anterior
print(cuadros)

#TUPLAS (INMUTABLES)
punto = (3,4,3)
print(punto[0],punto[1]) #imprime 3 4
punto.index(3) #devuelve la posición del primer tres: 0
#punto.index(3,4) #devuelve la posición del cuatro a partir del punto 3: 1
#punto.index(3,4,3) #se le ha añadido principio y fin a la búsqueda, devuelve: 1
#Esto de arriba no funciona por alguna razón !!!!!!!!!


#DICCIONARIOS
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"]) #imprime Juan

print(persona.keys()) #imprime una lista de llaves, "nombre", "edad" y "ciudad"
print(persona.values()) #imprime los valores de las llaves, "Juan", "25", "Madrid"
print(persona.items()) #imprime llave y valor, ambos

persona.update({"profesión":"Ingeniero"}) #añade una llave y un valor
print(persona.items())
print(persona)


#CONJUNTOS
cjt1 = {1,2,3}
cjt2 = {3,4,5}
cjt3 = {"Ciruelas","Manzana","Alcachofa"}

union = cjt1 | cjt2 #elementos diferentes: 1,2,3,4,5
interserccion = cjt1 & cjt2 #elementos iguales: 3
diferencia = cjt1 - cjt2 #le quita a uno los elementos del otro: 1,2
diferencia_simetrica = cjt1 ^ cjt2 #excluye los elementos repetidos: 1,2,4,5

cjt3.add("Tomate")
cjt3.remove("Tomate") #Si no hay "Tomate" genera un error
cjt3.discard("Tomate") #Si no hay "Tomate" no pasa nada
cjt3.clear() #vacía toda la lista