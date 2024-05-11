import os

#menu principal
respuesta = -1
while(respuesta != 0):
    print("Elija una opción")
    print("1. calculadora")
    print("2. Ver mi IP")
    print("3. Administrador de tareas")
    print("4. Apagar equipo en 5 minutos")
    print("5. cancelar apagado")
    print("o. salir")
    respuesta = int(input(" | "))
    if( respuesta == 1):
        os.system('calc')
    elif(respuesta == 2):
        os.system('ipconfig')
    elif(respuesta ==3 ):
        os.system('taskngr')
    elif(respuesta==4):
        os.system('shutdown -s -t 300 ')
    elif(respuesta == 5):
        os.system(' ')
    else:
        "no se ha seleccionado nada"

