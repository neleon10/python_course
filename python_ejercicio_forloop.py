#Crea una función que compare dos listas. True si son iguales y False si son diferentes. 

def comparaListas (a,b):
    if (len(a))!= (len(b)):
        return False
    else:
        for i in range (0,len(a)):
            if (a[i]) != b[i]:
                return False
    
    return True

listaA=["Ana","Pedro","Martin"]
listaB=["Ana","Pedro","Martin"]

print(comparaListas(listaA,listaB))