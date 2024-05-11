notas =[]

for x in range(3):
    nota= 0
    while nota<1 or nota>5:
        nota = int(input(f"Ingrese la nota {x+1}: "))
    notas.append(nota)
 
suma = 0
for x in range (3): 
    suma= suma + notas[x]
promedio=suma/3
print( "promedio de notas: %.1f"%(promedio))

print("Estado")
if(promedio>1.7):
    print("aprovado")
else:
    print("reprobado")

