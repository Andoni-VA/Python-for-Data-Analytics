#CREAR MÓDULOS PROPIOS
#este se llama mod_prop.py

def saludar(nombre):
    print(f"Hola, {nombre}!")
def calcular_suma(a,b):
    return a + b

# para importar el módulo en otro archivo: 
# import mod_prop
# mod_prop.saludar("Juan")
# res = mod_prop.calcular_suma(5,6)
# print(res)