

def evaluarAlumno(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Desaprobado"
    return valoracion

print (evaluarAlumno(int(input("Ingrese nota: "))))
