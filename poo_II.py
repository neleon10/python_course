class Person ():
    def __init__(self, name, lastName, age, gender):  # asi de define un constructor
        self.nombre = name
        self.apellido = lastName
        self.edad = age
        self.genero = gender

    def saludar(self):
        return "Hola me llamo " + self.nombre +" " + self.apellido + " ¿todo bien?"

    def camina(self):
        return "Hola soy "+ self.nombre + " y estoy caminando."

    def getDatos(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + \
            " Edad : " + str(self.edad) + " Genero: " + self.genero


person1 = Person("Carlos", "Vazquez", 39, "Maculino")

print(person1.getDatos())
print(person1.camina())
print(person1.saludar())
