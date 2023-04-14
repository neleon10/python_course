
""" CONTINUE:  en realidad no ejecuta el bucle si se cumple una condicion """


""" PASS: es para no ejecutar el bucle o lo que sea que no quiera ejecutar """

"""ELSE: cuando un ELSE está dentro de un BUCLE (no un IF) """


nombre = 'Carlos Osvaldo   Vazquez    Nosetto'

print (len(nombre))

counter = 0

for i in nombre: 
    if i == " ":
        continue
    
    counter += 1    

print(counter)


""" ejemplo de ELSE en bucle """

email=input('Introduce tu email: ')


for i in email:
    if i =='@':
        arroba = True
        break
    
else:
    arroba = False

print(arroba)   