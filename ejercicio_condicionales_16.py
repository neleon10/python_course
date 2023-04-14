

print("Bienvenido a tu programa que te calcula la renta. ")
renta=float(input("Introduzca el monto de la renta para saber su valor impositivo: "))

if renta < 0:
    print ("El programa no acepta números negativos. ")
elif renta < 15000 and renta >= 0:
    print("A la renta " + str(renta)+ " le corresponde un 7 %")
elif renta <= 18000 and renta > 15001:
    print("A la renta " + str(renta)+ " le corresponde un 15 %")
elif renta <= 35000 and renta > 18001:
    print("A la renta " + str(renta)+ " le corresponde un 21 %")
elif renta <= 70000 and renta > 35001:
     print("A la renta " + str(renta)+ " le corresponde un 35 %")
else:
    print("A la renta " + str(renta)+ " le corresponde un 45 %")
