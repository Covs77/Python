''' Ejercicio 1 Programación orientada a objetos'''
''' Covadonga Leguina Roig'''
'''Creación de clases e impresión por pantalla'''

class Persona:
  def __init__ (self, nombre, edad, ape, calle):
    self.nombre = nombre
    self.edad = edad
    self.ape = ape
    self.calle = calle

  def __str__(self):
    return f"Hola, me llamo {self.nombre} {self.ape} y tengo {self.edad} años y vivo en el calle {self.calle}..." 

p1 = Persona("Cova", 48, "Leguina", "Cuba")
p2 = Persona("Ana", 23, "Martin", "Albacete")


''' Impresión de los atributos por separado'''
print("\nImpresión de los atributos por separado:\n")
print(p1.nombre)
print(p1.ape)
print(p1.edad)
print(p1.calle)

''' Impresión con la función de formateo '''
print("\nImpresión de los atributos con la función de formateo de atributos:\n")
print(f"Hola, me llamo {p1.nombre}  {p1.ape} y tengo {p1.edad} años")

'''Impresión con la función __str__ '''
print("\nConcatenación de impresión de atributos con __str__:")
print(p1)
print(p2)