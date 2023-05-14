class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado=False

    def arrancar(self):
        self.arrancado = True
    def detener(self):
        self.arrancado = False
    def estadoDelCoche(self):
        if(self.arrancado):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

ferrari = Coche()
porsche = Coche()

porsche.arrancar()
print("El ancho del chasis es: ", ferrari.anchoChasis)
print(ferrari.estadoDelCoche())
print(porsche.estadoDelCoche())