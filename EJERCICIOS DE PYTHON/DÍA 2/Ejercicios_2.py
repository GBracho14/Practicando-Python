#EJERCICIO 2
###############################################################################

#1 - ¿Cuáles de los siguientes Strings son correctos?

#a) "Hoy es un gran día para programar" - Correcta
#b) 'El cielo está nublado" - Incorrecta
#c) '¿Qué día es hoy?' - Correcta
#d) "Mañana, en inglés se dice "morning"" - Incorrecta

#2 - ¿Qué error devuelven los strings que están mal escritos?

#R: Syntax error

#3 - Imprime en la consola el número de caracteres que tiene la palabra "automáticamente".
#    Lo puedes hacer con variable o directamente en un print().
'''
palabra = len("automáticamente")
print(f"El número de caracteres de la palabra 'automáticamente', es: {palabra}")
'''
#4 -  ¿Sabrías mostrar en la consola solo el carácter de la "a" con acento de "automáticamente"?
#     Lo debes hacer mediante las posiciones de string
'''
letra = ("automáticamente" [5])

print(f"La letra selecccionada es: {letra}")
'''
#5 - Realiza la operación de 10 elevado a 5 con el uso del operador exponente
'''
num = 10
exp = 5
operacion = num ** exp
print(f"El resultado es: {operacion}")
'''
'''
#6 - Cómo harías esta misma operación sin el operador exponente?
operacion = num * num * num * num * num 
print(f"El resultado es: {operacion}")
'''
#7 - ¿En qué dos estados puede estar un booleano?

#R: True o False

#8 - Muestra en la consola el tipo de dato que contiene esta variable:
'''
numero_1 = 675.87

print(type(numero_1))
'''
#9 - Muestra la cantidad de dígitos que tiene el siguiente número utilizando la función "len()"
'''
numero = 768763843
print(len(str(numero)))
'''
#10 - Haz que los siguientes datos float se conviertan en integer mediante la conversión de tipos
'''
numero_1 = float("14.527")
numero_2 =  float("560.92")

print(int(numero_1))
print(int(numero_2))
'''
#11 - Redondea estos números con la cantidad de decimales indicada en los comentarios e 
#     imprímelos en la consola
'''
num_1 = 10.897654876534 # 3 decimales
num_2 = 7674.7886 # 2 decimales
num_3 = 68754.78 # 1 decimal

print(round(num_1, 3))
print(round(num_2, 2))
print(round(num_3, 1))
'''

#12 - ¿Cuál es la diferencia entre el operador módulo y floor división?
'''
El operador "Módulo" se encarga de retornar el residuo de la división, mientras que 
el operador "floor division" obtiene el consiente con decimales de la división
'''

#13 - Asigna con los operadores de asignación de incremento o decremento los siguientes 
#     valores indicados en los comentarios
'''
num_1 = 10 # +60
num_2 = 24 # -100
num_3 = 65.67 # +4.33

num_1 += 60
num_2 -= 100
num_3 += 4.33

print(num_1, num_2, num_3)
'''

#14 - Mediante la técnica de formateo de strings(recuerda el prefijo f) muestra
#     literalmente todos estos valores en una frase en el print(), sin utilizar la 
#     concatenación
'''
numero_1 = 4
numero_2 = 769.97
texto = "am I a string"
decision = True

print(f"El valor {numero_2} es bastante más grande que {numero_1}. ¿{texto}? The answer is {decision}")
'''