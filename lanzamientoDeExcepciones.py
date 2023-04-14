import math
def calculaRaizCuadrada(numero):
    if(numero < 0):
        raise ValueError("El numero es menor a cero")#es para mandar mensaje de error
    else:
        return math.sqrt(numero)


numeroUsuario = (int(input("Introduce el numero: ")))

#me obliga a meter un try catch --> en python try except para que no caiga el programa
try:
    print(calculaRaizCuadrada(numeroUsuario))
except ValueError:
    print("error numero negativo")

print("el programa no se rompe continua...")