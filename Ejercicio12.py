numero_1= int(input("ingrese el primer numero: "))
numero_2= int(input("ingrese el primer numero: "))
if (numero_1 > numero_2):
    print("{}es mayor a {}".format(numero_1, numero_2))
    if(numero_1 %2==0):
        print("el numero es par")
    else:
        print("el numero es impar")
elif(numero_1 < numero_2):
    print("{} es mayor a {})el numero ".format(numero_2, numero_1))
    if(numero_2 % 2 ==0):
        print("el numero es par")
    else:
        print("el numero es inmpar")
else:
    print("los numers ingresados son iguales")

#2
usuario= input("ingrese su usuario: ")
password= input("ingrese su contraseña: ")
if( usuario == "admin" and password == "12345"):
    print("Acceso correcto") 
else:
    print("Acceso denegado ")