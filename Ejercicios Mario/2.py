#A modo de orientación cada enunciado va a contar con un refinamiento global en el que se enuncie la posible solución al problema planteado en cada caso o el mejor método de resolución considerado. Todos los enunciados son trabajados con cadenas insertadas y manipuladas como conjuntos.

#Ejercicio 2: Enunciado
#Ingresar una palabra y determinar el número de ocurrencias de un símbolo dado.

#Refinamiento global: Se excluyen las llaves y la coma como en los enunciados anteriores, por lo que sólo hay que pedirle al usuario que ingrese un símbolo (validado en la linea 19) y se evalúa si se cumple con tener llaves y coma. Posteriormente, si la respuesta es verdadera, se le quitan las llaves y se contabiliza si el elemento analizado forma parte de la cadena.

def ocurrencias(palabra, simbolo):
    contador = 0
    for elemento in palabra:
        if elemento != ',' and elemento != '{' and elemento != '}':
            if elemento == simbolo:
                contador += 1
    return contador

palabra = input("Ingrese la palabra (entre llaves y separado por comas): ")
simbolo = input("Ingrese el símbolo que desea contar: ")

if len(simbolo) != 1:
    print("Ingrese un único símbolo para contar: ")
else:
    if len(palabra) < 2 or palabra[0] != '{' or palabra[-1] != '}':
        print("El formato de la palabra es incorrecto.")
    else:
        palabra = palabra[1:-1]        
        ocurrencias = ocurrencias(palabra, simbolo)
        if(ocurrencias > 0):
            print(f"El símbolo '{simbolo}' aparece {ocurrencias} veces en la palabra.")
        else:
            print(f"El símbolo '{simbolo}' NO aparece en la palabra.")        