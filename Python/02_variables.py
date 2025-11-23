# Variables

myVariable1 = 10
print(myVariable1)
myVariable = "Ahora soy una cadena"
print(myVariable)

de_int_a_string= str(myVariable1)  # Convierte el entero a cadena
print(de_int_a_string)
print(type(de_int_a_string))  # Muestra el tipo de dato de la variable

# ALgunas funciones
print(len(de_int_a_string))  # Muestra la longitud de la cadena o sea cuenta cuantos caracteres o letras tiene
print("-"*100)  # Imprime 100 guiones
# Varias variables en una línea
nombre, apellido, edad = "Arturo", "Ojeda", 22
print(nombre)
print(apellido)     
print(edad) 

print("="*50)

nombre= input("Escribe tu nombre: ")  # input siempre devuelve una cadena
print("Hola " + nombre + ", bienvenido a Python")
edad= int (input("Escribe tu edad: "))  # Convierte la cadena a entero


