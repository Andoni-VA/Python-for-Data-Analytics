#INPUTS Y OUTPUTS

nombre = input("Ingresa tu nombre:  ")
#input() siempre devuelve una cadena de texto, para pasar a otro tipo de valor
#se tendría que hacer una conversión explícita, int() o float()

edad = int(input("Ingresa tu edad: "))

print("Hola, " + nombre + "!")

if edad>=18:
    print("Eres mayor de edad!")
else:
    print("Eres menor de edad!")

#se puede usar f-string para meter variables dentro de una cadena de texto
#print(f"tal")
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")