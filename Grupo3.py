# en esta funcion le estamos pidiendo al usuario q ingrese los numeros
def Ingresar_Numeros():
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el primer numero: "))
    return numero1, numero2

# en esta funcion estamos sumando los numeros ingresados por el usuario


def suma(numero1, numero2):
    resultado = numero1+numero2
    return resultado


# aqui estamos llamando las funcfiones para ingresar los numeros y imprimir el resultado
valor = Ingresar_Numeros()
print(suma(valor[0], valor[1]))


def multiplicacion(numero1, numero2):
    print("Vamos a hacer una multiplicacion")
    resultado = numero1*numero2
    print("El resultado de la multiplicacion es: ", resultado)
