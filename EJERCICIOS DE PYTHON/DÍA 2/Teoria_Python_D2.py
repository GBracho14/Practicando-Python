#STRINGS
##############################################################################
#Tipos de Strings
'''"
String en comillas dobles"
'String en comillas simples'
'''

#Forma incorrecta de utilizar comillas en un string
'''
print(""Blue" es azul en español.")
print(''Red' es rojo en español.')
'''

#Forma correcta de utilizar comillas
'''
print("'Blue' es azul en español.")
print('"Red" es rojo en español.')
'''

#FUNCIÓN "Len()"
#devuelve número de caracteres que tiene un string
#IMPORTANTE! Solo funciona con strings
    #print(len("Amarillo"))
#Instanciando un String y devolviendo caracter según su posición en la cadena:
'''color = "Morado"
print(color[2])'''

#INTEGERS
###############################################################################
#OPERACIONES NUMÉRICAS UTILIZANDO VARIABLES:
'''
num_1 = 400
num_2 = 100

#Suma
resultado = num_1 + num_2
print(resultado)

#Resta
resultado = num_1 - num_2
print(resultado)

#Multiplicación
resultado = num_1 * num_2
print(resultado)

#División sin decimales
resultado = num_1 // num_2
print(resultado)

#División con decimales
resultado = num_1 / num_2
print(resultado)

#Módulo: Devuelve el residuo de la división
resultado = num_1 % num_2
print(resultado)

#Potencias
potencia = 3
base = 3
resultado = potencia ** base 
print(resultado)'''

#OPERACIONES ARITMÉTICAS
'''
operacion_1 = 10 + 56 * 89 - 3 / 2
operacion_2 = 10 + 56 * (89 - 3) / 2

print(operacion_1)
print(operacion_2)
'''

#SEPARADORES EN NÚMEROS
#Sirve para no equivocarnos en el ingreso de ciertas cifras 
'''
numero_1 = 2_347_823_472_928_342_309_238_423
print(numero_1)
'''

#FLOAT
###############################################################################
'''
numero_1 = 56.879
numero_2 = 10
print(numero_1)
print(numero_2)
'''

#BOOLEANO
###############################################################################
'''
decision_Af = True
decision_fa = False
'''

#FUNCIÓN "type()"
#Sirve para devolver el tipo de dato que contiene una variable
'''
numero_1 = 4
numero_2 = 769.97
texto = "Soy un string."
decision = True

print(type(numero_1))
print(type(numero_2))
print(type(texto))
print(type(decision))
'''

#TRANSFORMACIÓN DE DATOS
#Integer a String
'''
numero = 23984293420323942
digitos = str(numero)

print(len(digitos))

#String a Integer
numero_1 = "10"
numero_2 = "50"

suma = int(numero_1) + int(numero_2)
  
print(suma)

#String a Float
numero_1 = "10.56"
numero_2 = "50.9"

suma = float(numero_1) + float(numero_2)

print(suma)
'''
#Suma Float con resultado Integer
'''
numero_1 = "10.56"
numero_2 = "50.9"

suma = float(numero_1) + float(numero_2)

print(int(suma))
'''
#Función "round()":  Redondeando Float
'''
multiplicacion = 7.2334 * 6.82377428

print(round(multiplicacion))
#Redondear a una cantidad específica de decimales
print(round(multiplicacion,2))
'''
#OPERADORES DE ASIGNACIÓN: Incremento y decremento
#Incremento
'''
numero_1 = 10

numero_1 += 10
print(numero_1)

#Decremento
numero_1 -= 10
print(numero_1)
'''
#Realizando Prints con concatenaciones entre String e Integer
'''
suma = 90 + 67

print(f"El resultado de la suma es: {suma}")
'''