calificaciones=[2,5,5,4,1]
nombres=["Moisés", "Camila", "fernanda","Pablo", "tania"]
lista_variada=[ True, 10.5, "abc", [0,1,1]]
print("Estudiante:" , nombres[2])
print("calificacion:" ,calificaciones[-2] )
print("lista dentro de la otra" , lista_variada)
print("Imprimir un rango o slices" ,nombres[1:2])
nombres.append("Anibal")
print(nombres)
nombres.remove("Pablo")
print(nombres)

Colores=("Azul" , "Verde" ,"Rojo" ,"Amarillo" ,"Blanco" ,"Negro" ,"Gres")
print("Color" , Colores[3])

producto={"manzana" :5600, "mandarina" :12000, "kiwi" :25000}
print("Precio de la manzana en Gs. " , producto["manzana"])
print("Precio", producto)