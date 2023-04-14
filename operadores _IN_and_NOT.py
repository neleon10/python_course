trabajadores=["Nela", "Pedro" , "Sandra" , "Laura" ,"Raquel","Carlos"]
nombre=input("Ingrese el nombre que busca: ")
if  nombre in trabajadores:
    print("Sí, está en la lista.")
else:
    print("No se encuentra en la lista. ")

#---------------- 2 ------------
lenguajes="Java, Python, SQL, C#, C++, C, JavaScript, HTML" #OJO no es lista es STRING.
nombrePrograma=input("Enter the name of the Language you're looking for: ")
if nombrePrograma not in lenguajes:
    print("No está en el STRING")
else:
    print("Sí está en el STRING")