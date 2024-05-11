import random

while True:
    aleatorio= random.randrange(0, 3)
    elijePc =""
    print("1. PIEDRA")
    print("2. PAPEL")
    print("3. TIJERA")
    opcion= int (input("Elege tu opción"))
     
    if opcion ==1:
        elijeUsuario ="PIEDRA"
    elif opcion ==2:
        elijeUsuario ="PAPEL"
    elif  opcion ==3:
        elijeUsuario ="TIJERA"
    print("Elejiste: ", elijeUsuario )

    if aleatorio==0:
     elijePc ="PIEDRA"
    elif opcion ==1:
      elijePc ="PAPEL"
    elif  opcion ==2:
      elijeUsuario ="TIJERA"
    print(" La maquna elijio: ", elijePc )
    print("...")
    if elijePc == "PIEDRA" and elijeUsuario =="PAPEL":
       print("Ganaste, PAPEL envuelve PIEDRA")
    elif elijePc == "PAPAL" and elijeUsuario == "TIJERA":
        print("Ganaste, TIJERA corta PAPLE ")
    elif elijePc == "TIJERA" and elijeUsuario == "PIEDRA":
        print("Ganaste, PIEGRA machaca TIJERA")
    if elijePc == "PAPEL" and elijeUsuario =="PIEDRA":
       print("Perdiste , PAPEL envuelve PIEDRA")
    elif elijePc == "TIJERA" and elijeUsuario == "PAPEL":
      print("Perdiste , TIJERA corta PAPLE ")
    elif elijePc == "PIEDRA" and elijeUsuario == "TIJERA":
       print("Perdiste, PIEDRA machaca TIJERA")
    elif elijePc == elijeUsuario:
       print("empate")



