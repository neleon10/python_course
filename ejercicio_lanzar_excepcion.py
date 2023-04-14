# pide 10 nombres
# los nombres de guardan en una lista
# si el nombre esta lanza: “Error. Este nombre ya se ha introducido”

#Esto es una forma de hacerlo, hay varias

listaDeNombres = []


def nombreIngresado(nombre):
    if nombre in listaDeNombres:
        raise ValueError("El nombre esta en la lista")
    else:
        listaDeNombres.append(nombre)
        if len(listaDeNombres) < 10:
            nombreIngresado(input("Introduce otro nombre: "))
    return listaDeNombres

try:
    print(nombreIngresado(input("Introduce el nombre: ")))
except ValueError as e:
    print("Error:",e)
