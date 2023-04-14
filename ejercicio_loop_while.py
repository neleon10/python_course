import random
numeroAleatorio=random.randint(1,100)
num=int(input("Enter a number to guess the Random Number: "))
intentos=1


while num!=numeroAleatorio:
    if num > numeroAleatorio:
        print("THE Random number is MINOR, try again.")
    else:
        print("THE Random number is MAJOR, try again.")
    
    num=int(input("Enter another number: "))
    intentos+=1  

print("Congrats! you guessed the number. ")
print ("The number is " + str(numeroAleatorio) + " and you did it in " + str(intentos) + " times. ")