#A modo de orientación cada enunciado va a contar con un refinamiento global en el que se enuncie la posible solución al problema planteado en cada caso o el mejor método de resolución considerado. Todos los enunciados son trabajados con cadenas insertadas y manipuladas como conjuntos.

#Ejercicio 1: Enunciado
#Ingresar dos palabras y determinar si una es la inversa de la otra.

#Refinamiento global: El enunciado plantea una problemática de forma directa, comparar una cadena con otra que se encuentre al revés, lo cuál se soluciona de manera sencilla a través de la expresión palabra1 = palabra2[::-1], que, a través de la sintaxis de python, permite hacer la comparación entre dos elementos, siendo que el segundo se encuentra siendo analizado en sentido contrario a como se encuentra ingresado en el código. 
# Para el funcionamiento del código se crea una función que devuelve un resultado booleano, propio de hacer la conparación antes mencionada. Posteriormente sólo queda llamar a la función definida para el caso y dejar que se evalúe con los parámetros leídos, que fueron previamente modificados, ya que se les extrajeron los corchetes, con la expresión palabra1 = palabra1[1:-1], que iguala palabra1 a sí misma pero sin las posiciones 0 y la última, que son en las que se encuentran las llaves del conjunto.

def comparacionInversa(conj1, conj2):
    return conj1 == conj2[::-1]

conj1 = input("Ingrese la primera palabra (entre llaves): ")
conj2 = input("Ingrese la segunda palabra (entre llaves): ")

conj1 = conj1[1:-1]
conj2 = conj2[1:-1]

if comparacionInversa(conj1, conj2):
    print("Una palabra es la inversa de la otra.")
else:
    print("Las palabras no son inversas entre sí.")


#3- Dado un alfabeto, determinar si las palabras ingresadas, están formadas por dicho alfabeto (mostrar mensaje OK o NO OK, según el caso) . En el caso de contener otros elementos que no pertenezcan al alfabeto, mostrar cuales son los elementos diferentes

# def comprobarAlfabeto():
#     alf = input("Ingrese las letras que componen al alfabeto: ")
#     cadena = input("Ingrese el texto para analizar: ")
#     errores = []
#     bandera = 0
#     i = 0
#     for i in range(len(cadena)):
#         if((cadena[i] not in alf) & (cadena[i] != ' ')):
#             bandera = 1
#             errores += cadena[i]
#             break
#     if(bandera == 1):
#         print("NO OK")
#         print("Los caracteres erroneos son: ",errores)
#     else:
#         print("OK")
        
# comprobarAlfabeto()

# def validar_palabra(palabra, alfabeto):
#     elementos_diferentes = []
#     for elemento in palabra:
#         if elemento != ',' and elemento != '{' and elemento != '}':
#             if elemento not in alfabeto:
#                 elementos_diferentes.append(elemento)
#     return elementos_diferentes

# alfabeto = input("Ingrese el alfabeto (entre llaves y separado por comas): ")
# palabra = input("Ingrese los elementos (entre llaves y separado por comas): ")

# if len(alfabeto) < 2 or alfabeto[0] != '{' or alfabeto[-1] != '}':
#     print("El formato del alfabeto es incorrecto.")
# else:
#     alfabeto = set(alfabeto[1:-1].split(','))

#     if len(alfabeto) == 0:
#         print("El alfabeto no puede estar vacío.")
#     else:
#         elementos_diferentes = validar_palabra(palabra, alfabeto)

#         if len(elementos_diferentes) == 0:
#             print("OK")
#         else:
#             print("NO OK")
#             print("Elementos diferentes:", elementos_diferentes)
