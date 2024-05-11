class Persona: 
    nombre = None
    edad = None
    
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"{self.nombre}, edad: {self.edad}"    

class Empleado(Persona):
    sueldo_bruto = None
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo

    def mostrar(self):
        return super().mostrar() + f" SN: {self.calcular_salario_neto()}"
    
    def calcular_salario_neto(self):
        return self.sueldo_bruto * 0.9
    
class Directivo(Persona):
    categoria = None
    
    def __init__(self, nombre, edad, categoria):
        super().__init__(nombre, edad)
        self.categoria = categoria

    def mostrar(self):
        return super().mostrar() + f" Categoria: {self.categoria}"
    
class Cliente(Persona):
    telefono_de_contacto = None
    
    def __init__(self, nombre, edad, telefono):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono
    
    def mostrar(self):
        return super().mostrar() + f" Telefono: {self.telefono_de_contacto}"
    
class Empresa:
    nombre = None
    
    def asignar_nombre(self, nombre):
        self.nombre = nombre
        return self.nombre
        
if __name__ == '__main__':
    emp = Empleado("Empleado: Maria", 45, 450000)
    di = Directivo("Directivo: Jessica", 50, "Gerente general")
    cli = Cliente("Cliente: Luis", 34, "0982 345 675")
    
    print(emp.mostrar())
    print(di.mostrar())
    print(cli.mostrar())
    