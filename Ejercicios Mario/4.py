#A modo de orientación cada enunciado va a contar con un refinamiento global en el que se enuncie la posible solución al problema planteado en cada caso o el mejor método de resolución considerado. Todos los enunciados son trabajados con cadenas insertadas y manipuladas como conjuntos.

#Dado dos lenguajes como entradas (L1 y L2) y un texto que contenga concatenaciones que pueden obtenerse de los lenguajes de entrada, verificar que las concatenaciones ingresadas se correspondan con los lenguajes L1 y L2


def productoConjuntos(texto, conj1, conj2):
    concatenaciones = texto[1:-1].split(',')  # Separar el texto en concatenaciones

    for concatenacion in concatenaciones:
        val1 = all(subcadena in conj1 for subcadena in concatenacion.split('+'))
        val2 = all(subcadena in conj2 for subcadena in concatenacion.split('+'))

        if val1 and val2:
            print(f"La concatenación '{concatenacion}' cumple con ambas reglas.")
        elif val1:
            print(f"La concatenación '{concatenacion}' cumple con L1 pero no con L2.")
        else:
            print(f"La concatenación '{concatenacion}' no cumple con L1.")

conj1 = {"ca", "ma"}  # Ejemplo: Conjunto de cadenas para L1
conj2 = {"nta", "sa"}  # Ejemplo: Conjunto de cadenas para L2

texto = input("Ingrese el texto con concatenaciones (entre llaves y separado por comas): ")
productoConjuntos(texto, conj1, conj2)


