name, surname, age = "Arturo", "Ojeda", 22

print( "Mi nombre es {} {} y tengo {} años".format(name, surname, age) )
print( f"Mi nombre es {name} {surname} y tengo {age} años" )
print( "Mi nombre es %s %s y tengo %d años" % (name, surname, age) )
print( "Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años" )  


ejemplo_de_cadena = "hola mundo"
print( ejemplo_de_cadena.capitalize() ) # Primera letra mayuscula
print( ejemplo_de_cadena.upper() )  # Convierte a mayusculas
print( ejemplo_de_cadena.lower() )  # Convierte a minusculas
print( ejemplo_de_cadena.count("o") ) # Cuenta cuantas veces aparece la letra o
print( ejemplo_de_cadena.replace("mundo", "Python") ) # Reemplaza la palabra mundo por Python
print( ejemplo_de_cadena )  # La cadena original no cambia