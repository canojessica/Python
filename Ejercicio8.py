#strings o cadenas de texto
nombre="tu nombre "
apellido='apellido '
print(nombre+""+apellido)
texto=" este texto\ntiene saldo de linea y \ttabulacion"
print(texto)
#formateo
user, password, email= "Jessica", 12345, "canoj706@gmail.com"
print("su usuario y contraseña son {} {} y su emai {} ".format(user, password, email))
print("su usuario y contraseña son %s %d y su email %s "%(user, password, email))
print(f"su usuario y contraseña son {user} {password} y su email {email} ")