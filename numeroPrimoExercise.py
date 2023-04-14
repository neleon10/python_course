num = int(input("Ingrese número: "))
num2 = int(input("Ingrese el segundo numero: "))

def primo (numero):
    for n in range (2,numero):
        if numero % n==0:

         return False
    
    print(str(numero) + ' es primo.' )
    return True

for i in range (num, num2):
    primo(i)
    