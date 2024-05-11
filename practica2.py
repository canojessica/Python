import time
dato_acceso= { "admi":"1234", "pepe":"5678", "jessica": "9123"}
usuario=input("ingrese usuario")
passoword=input("ingrese contraseña")

if usuario in dato_acceso:
    print("usuario correcto")
    time.sleep(1)
    print("verificando contraseña")
    time.sleep(1)
    if passoword ==dato_acceso[usuario]:
        print("acceso correcto")
    else:
        print("error de contraseña")
else:
    print("error de datos")