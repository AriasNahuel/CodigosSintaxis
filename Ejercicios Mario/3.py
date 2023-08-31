#A modo de orientación cada enunciado va a contar con un refinamiento global en el que se enuncie la posible solución al problema planteado en cada caso o el mejor método de resolución considerado. Todos los enunciados son trabajados con cadenas insertadas y manipuladas como conjuntos.

#Ejercicio 3: Enunciado
#Dado un alfabeto, determinar si las palabras ingresadas, están formadas por dicho alfabeto (mostrar mensaje OK o NO OK, según el caso) . En el caso de contener otros elementos que no pertenezcan al alfabeto, mostrar cuales son los elementos diferentes.

#Refinamiento global: Trabajando igualmente con funciones, en este caso se agrega el símbolo de la coma, ya que se puede ingresar más de un símbolo como parte de los caracteres del alfabeto. Teniendo el alfabeto definido, se hace un recorrido de la cadena ingresada para ser analizada, corroborando si los caracteres ingresados, que son distintos de comas y llaves, se encuentran en el alfabeto almacenado. Además se agrega una validación en la que se evalúa si el alfabeto no se encuentra entre llaves y si su longitud es menor que 2, ya que por cuestiones de funcionamiento debe tener ambas llaves y sólo con eso ya posee 2 caracteres, por lo que si se trata de un alfabeto vacío no va a entrar en la ejecución.

def comprobarAlfabeto(palabra, alfabeto):
    errores = []
    for elemento in palabra:
        if elemento != ',' and elemento != '{' and elemento != '}':
            if elemento not in alfabeto:
                errores.append(elemento)
    return errores

alfabeto = input("Ingrese el alfabeto (entre llaves y separado por comas): ")
palabra = input("Ingrese los elementos (entre llaves y separado por comas): ")

if len(alfabeto) < 2 or alfabeto[0] != '{' or alfabeto[-1] != '}':
    print("El formato del alfabeto es incorrecto.")
else:
    alfabeto = set(alfabeto[1:-1].split(','))#se convierte el alfabeto, quitándole las llaves y las comas mediante el uso del método split.

    if len(alfabeto) == 0:
        print("El alfabeto no puede estar vacío.")
    else:
        errores = comprobarAlfabeto(palabra, alfabeto)

        if len(errores) == 0:
            print("OK")
        else:
            print("NO OK")
            print("Los caracteres erroneos son: ", errores)
