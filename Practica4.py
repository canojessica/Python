def ordenar_lista(lista, orden):
    contador= 0
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            if lista[y] < lista [y+1]:
                aux=lista[y]
                lista[y]= lista[y+1]
                lista[y+1]= aux
            contador+=1
        
    print("Contador: ", contador)
    return lista


lista_original= [2,3,5,67,45,32,6,4,32,43,2]
print("Lista original: ", lista_original)

lista_ordenada =ordenar_lista(lista_original, "asc")
print("lista ordenada", lista_ordenada)