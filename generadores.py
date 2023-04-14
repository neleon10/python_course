""" 
Los generadores crean objetos iterables 
En vez de return, usamos YIELD. 
Si queremos acceder a un objeto iterable dentro de otro objeto iterable el generador
nos va a ayudar a simplficar la tarea.
"""
#Los parametros con el * indican que son parametros indeterminados y los tomará dentro de una tupla

def capitales_del_mundo(*ciudades):
    for capital in ciudades:
        yield from capital


        #for letras in capital:
            #yield letras

#Atencion si uso el YIELD FROM reemplaza el for anidado.


#En capitales_devueltas voy a tener almacenado las capitales en forma de tupla"

capitales_devueltas = capitales_del_mundo("Madrid","Roma","Pekin","Buenos Aires")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))