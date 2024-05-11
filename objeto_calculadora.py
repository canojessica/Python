class calculadora:
    numero1 = None
    numero2 = None

    resultado = None
    historial = None

    def __init__(self, n, m):
        self.numero1 = n
        self.numero2 = m
        self.resultado = 0
        historial= [ ]

    def suma (self):
        return self.numero1 + self.numero2
    def resta (self):
        return self.numero1 - self.numero2
    def multiplicacion (self):
        return self.numero1 * self.numero2

if __name__ =="__main__":
    casio=calculadora (45, 50)
    casio2=calculadora(34, 20)
    print("Suma= ", casio.suma() )
    print("Resta= ", casio.resta() )
    print("Multiplicacion ", casio.multiplicacion())
    print("Segunda calculadora: suma= ", casio2.suma())
    print("Segunda calculadora : resta= ", casio2.resta())
    print("segunda calculadora: multiplicacion= ", casio2.multiplicacion())