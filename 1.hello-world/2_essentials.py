# 1. Definir una función que toma dos parámetros y devuelve su suma.
def suma(a, b):
    return a + b

# 2. Pedir al usuario que ingrese dos números.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# 3. Llamar a la función suma y guardar el resultado en una variable.
resultado_suma = suma(num1, num2)

# 4.0 Imprimir el resultado de la suma usando "f-strings".
print(f"La suma de {num1} y {num2} es: {resultado_suma}")

# 4.1 Imprimir el resultado de la suma usando método format.
print("La suma de {} y {} es: {}".format(num1, num2, resultado_suma))

# 4.2 Imprimir el resultado de la suma, convirtiendoa  string los ints y concatenando.
print("La suma de " + str(num1) + " y " + str(num2) + " es: " + str(resultado_suma))

# 4.3 Imprimir el resultado de la suma, concatenando strings con ints.
print("La suma de", num1, "y", num2, "es: ", resultado_suma)

# 5. Crear una lista (array) de números.
numeros = [1, 2, 3, 4, 5]

# 6. Recorrer la lista y mostrar cada número.
print("Números en la lista:")
for numero in numeros:
    print(numero)

# 7. Verificar si un número está en la lista.
numero_buscado = int(input("Ingresa un número para buscar en la lista: "))
if numero_buscado in numeros:
    print(f"{numero_buscado} está en la lista.")
else:
    print(f"{numero_buscado} no está en la lista.")

# 8. Crear un diccionario con nombres y edades.
personas = {
    'Juan': 25,
    'María': 30,
    'Pedro': 22
}

# 9. Imprimir las claves del diccionario.
print("Nombres en el diccionario:")
for nombre in personas.keys():
    print(nombre)

# 10. Imprimir los valores del diccionario.
print("Edades en el diccionario:")
for edad in personas.values():
    print(edad)

# 11. Imprimir tanto las claves como los valores del diccionario.
print("Nombres y edades en el diccionario:")
for nombre, edad in personas.items():
    print(f"{nombre}: {edad}")

# 12. Crear una clase sencilla.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# 13. Crear un objeto de la clase Persona.
persona1 = Persona("Luis", 28)

# 14. Imprimir los atributos del objeto.
print(f"{persona1.nombre} tiene {persona1.edad} años.")

# 15. Agregar un nuevo nombre y edad al diccionario de personas.
nuevo_nombre = input("Ingresa un nuevo nombre: ")
nueva_edad = int(input("Ingresa una nueva edad: "))
personas[nuevo_nombre] = nueva_edad

# 16. Imprimir el diccionario actualizado.
print("Nombres y edades en el diccionario después de agregar una nueva persona:")
for nombre, edad in personas.items():
    print(f"{nombre}: {edad}")
5
# 17. Abrir un archivo en modo escritura y escribir contenido en él.
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un ejemplo de archivo creado desde Python.")

# 18. Leer el contenido del archivo y mostrarlo.
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
print("Contenido del archivo:")
print(contenido)

# 19. Importar un módulo y utilizar una función del mismo.
import random

# 20. Generar un número aleatorio entre 1 y 100 y mostrarlo.
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatorio generado: {numero_aleatorio}")