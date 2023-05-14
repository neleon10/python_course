class CuentaCorriente():
    def __init__(self,nCta,nombreYApellido,saldo):
        self.numeroDeCuenta = nCta
        self.titularDeCuenta = nombreYApellido
        self.saldoDeCuenta = saldo
    def getDatosCuenta(self):
        return "Numero de Cuenta: " + self.numeroDeCuenta + " " + "Titular: "  + self.titularDeCuenta + " " + "Saldo de la cuenta: " + str(self.saldoDeCuenta)
    def deposit(self,dineroExtra):
        if(dineroExtra >= 0):
            self.saldoDeCuenta = self.saldoDeCuenta + dineroExtra
        else:
            return "No se puede ingresar un valor menor a cero. "
    def withdraw(self,dineroARetirar):
        if(self.saldoDeCuenta <=0 or dineroARetirar < 0):
            return "no se puede retirar dinero de la cuenta. Su saldo es negativo"
        else:
            saldoFinal = self.saldoDeCuenta - dineroARetirar
            if(saldoFinal < 0):
                return "Lo siento no puede retirar esa cantidad de dinero, sus fondos son insuficientes"
            else:
                self.saldoDeCuenta = saldoFinal

cuenta1 = CuentaCorriente("123456789","Carlanga Bosetto",1500)

cuenta1.withdraw(1500)
print(cuenta1.getDatosCuenta())
