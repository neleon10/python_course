import sys

#suma
def suma(num1, num2):
    return num1+num2

#resta
def resta(num1, num2):
    return num1-num2

#Multiplicacion
def multiplica(num1, num2):
    return num1*num2

#Division
# Aqui tratamos la excepcion!
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir por cero.')
        return 'Error. '


intentos = 0
while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break

    except ValueError:
        intentos += 1

    print('No ha ingresado un valor correcto, tiene solo 3 intentos')
    print('El número de intentos es: ' + str(intentos))
    if intentos == 3:
        print('Lo siento, has consumido demasiados intentos. ')
        sys.exit()





#Once the numbres are chosen we continue executing the code here!
operacion = input(
    "Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")
