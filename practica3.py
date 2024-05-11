traductor= {'casa' :'house', 'lapiz':'pen'}

while True:
    palabra= input("Ingrese una palabra :")
    if palabra in traductor:
       print(traductor[palabra])
    elif palabra =="0":
       break
    else:
       resp= input("No existe la traduccion. ¿Desea agragar (s/n)?")
       if resp == "s":
          traduccion = input(f"Ingresa la traduccion de {palabra}")
          traductor[palabra]=traduccion 