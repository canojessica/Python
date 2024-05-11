from biblioteca import Biblioteca
from libros import Libro
if __name__ == '__main__':
    ejecutar = True
    print("- - - BIENVENIDO AL SISTEMA BIBLIOTECARIO - - -")
    while ejecutar:
        opcion =int (
            input(
                "¿Qué vas a hacer?: \n1-Crear biblioteca \n2-Agregar libro  \n3- ver catalogo \n4-Quitar libro \n5-salir\n: "
            )
        )
        if opcion == 1:
            nombre = input( "Nombre de la Biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print(
                "Se creo la biblioteca: {}".format(
                    biblioteca.consultar_nombre_biblioteca()
                )
            )
        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("autor: ")
            cantidad_de_paginas = input("Paginas: ")
            genero = input("Genero: ")
            sinopsis = input("sinopsis: ")

            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
            biblioteca.agregar_libro(libro)

        elif opcion ==3:
            print( " catalago de libros: ")
            for i in biblioteca.consultar_libros():
                print( i )

        elif opcion == 4:
            indice =input(" Id del libro a eliminar: ")
            biblioteca.quitar_libro(indice)
        elif opcion == 5:
            1
            print(" Gracia por visitar.  \n (°_°)")
            ejecutar = False
        else:
            print("opcion incorrecta")
