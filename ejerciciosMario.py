def comparacionInversa(palabra1, palabra2):
    return palabra1 == palabra2[::-1]

palabra1 = input("Ingrese la primera palabra (entre llaves): ")
palabra2 = input("Ingrese la segunda palabra (entre llaves): ")

palabra1 = palabra1[1:-1]
palabra2 = palabra2[1:-1]

if comparacionInversa(palabra1, palabra2):
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
