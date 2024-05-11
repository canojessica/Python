#cargar_imprimir una lista con funciones 
#DEFINIMOS UNA LISTA CON FUNCIONES 
lista = []

#definimos la funcion que permitira cargar la lista

def cargar_lista (dato):
    lista.append(dato)
#rescidir una cantidad indeterminado de argumentos 
def cargar_lista(*args):
    for arg in args:
        lista.append(arg)

def imprimir_lista():
    for item in lista:
        print(item, end=' | ')

#ejecutamos la funciones
cargar_lista(25)
cargar_lista(50)
cargar_lista(75)
cargar_lista(100)

#imprimir la lista 
imprimir_lista()

cargar_lista('A' , 'B' , 'C' , [125, 852, 963])
imprimir_lista()