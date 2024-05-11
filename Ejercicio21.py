def cargar_lista():
    lista = []
    while True:
        elemento = input("Ingrese un elemento o 'fin' para terminar): ")
        if elemento.lower() == 'fin':
            break
        lista.append(elemento)
    return lista

def imprimir_contenido_ordenado(lista):
    print("Contenido de la lista ordenado:")
    for elemento in sorted(lista):
        print(elemento)

def main():
    print("Bienvenido a la aplicación de lista")
    mi_lista = cargar_lista()
    imprimir_contenido_ordenado(mi_lista)

if __name__ == "__main__":
    main()