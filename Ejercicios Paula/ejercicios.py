# 1) Se desea eliminar los blancos de una frase dada terminada en un punto. Se supone que es posible leer los caracteres de la frase de uno en uno.
    # 2) Leer un carácter y deducir si está situado antes o después de la letra “m” en orden alfabético.
# 3) Leer los caracteres y deducir si están en orden alfabético.
# 4) Contar el número de letras “i” de una frase terminada en un punto. Se supone que las letras pueden leerse independientemente.
# 5) Contar el número de vocales de una frase terminada en un punto
# 6) Se desea contar el número de letras “a” y el número de letras “b” de una frase terminada en un punto. Se supone que es posible leer los caracteres independientemente.
# 7) Leer cien caracteres de un texto y contar el número de letras “b”.
# 8) Escribir un algoritmo para determinar si una cadena especificada ocurre en una cadena dada, y si es así, escribir un asterisco (*) en la primera posición de cada ocurrencia.
# 9) Escribir un algoritmo para contar el número de ocurrencias de cada una de las palabras 'a', 'an' y 'and' en las diferentes líneas de texto.
# 10) Diseñar una función que informe si una cadena es un palíndromo (una cadena es un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda).

#----------1----------
cadena = input("Ingrese una cadena: ")
def eliminarEspacio(cadena):
    cadenaFinal = ''
    for i in range(len(cadena)):        
        if cadena[i] == ' ':
            cadena = cadena[0:i] + cadena[i+1:len(cadena)] + ' '
    """ for i in range(len(cadena)):        
        if cadena[i] != ' ':
            cadenaFinal += cadena[0:i] """
    return print(cadena)        
        
eliminarEspacio(cadena)
#----------2----------
""" num = input("Ingrese una letra: ")
if num < 'm':
    print("El caracter está antes de la letra 'm'")
elif num > 'm':
    print("El caracter está después de la letra 'm'")
else:
    print("El caracter ingresado es la letra 'm'") """
"""     def comprobarAlfabeto():
    conj1 = input("Ingrese las letras que componen al alfabeto: ")
    #conj2 = input("Ingrese las letras que componen al alfabeto: ")
    conjTotal = ['{']
    lenConj1 = len(conj1) - 1
    i = 0
    for i+1 in range(lenConj1):
        conjTotal[i+1] += conj1[i]
    print(conjTotal)
    
    
comprobarAlfabeto() """
