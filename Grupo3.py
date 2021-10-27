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


def resta (numero1,numero2):

    resta=numero1-numero2
    print ("La resta es: ",resta)

resta(numero1,numero2)


def multiplicacion(numero1, numero2):
    print("Vamos a hacer una multiplicacion")
    resultado = numero1*numero2
    print("El resultado de la multiplicacion es: ", resultado)








def IngresarNumero(numero1,numero2):

    print("Que le importa sapo ")


    if numero2==0:
        print("el divisor no puede ser cero:git ")

    else:
        print(numero1/numero2)
