class Biblioteca:
    def __init__(self, nombre):
        self.nombre =nombre
        self.libros= []

    def consultar_nombre_biblioteca(self):
        return self.nombre
    
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def consultar_libros(self):
        return self.libros
    
    def consultar_libro(self, id):
        return self.libros[id]
    
    def quitar_libro(self, id):
        self.libros.pop(id)
    