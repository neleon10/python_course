
#Nunca puede haber un TRY sin un EXCEPT o FINALLY. Eso genera un error. 

def divide():
    try:
        op1 = float(input('Ingrese el numero requerido: '))
        op2 = float(input('Ingrese el segundo numero requerido: '))

        print('El resultado es: ' + str(op1/op2))

    except ZeroDivisionError:
        print('No se puede dividir por cero, esto genera un error. ')
    except ValueError: 
        print('El valor introducido debe ser numerico de otra forma genera error. ')

    finally:
        print('Estoy ejecutando el FINALLY, si se puede leer esta linea es porque siempre se ejecuta el finally.')

#se puede quitar los errores y agregar solo EXCEPT: en ese caso lo que podemos hacer es que 
# --> sin importar el tipo de error que tire lo captura igual. 

#Finally: lo que este dentro de esta instrucción siempre va a ejecutarse. Sirve para base de datos.
# --> siempre siempre se ejecuta el FINALLY , veremos el uso con la conexión a base de datos mas adelante.  


divide()
print('Calculo finalizado. ')
