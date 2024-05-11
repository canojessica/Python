#operaciones aritmeticos: resolver todas las operaciones 
print(" la suma de 10+4 es : ",10+4)
print(" la resta de 10-4 es : ",10-4)
print(" la multiplicacion de 10*4 es : ",10*4)
print(" la divicion de 10/4 es : ",10/4)
print(" el resto de 10/4 es : ",10%4)
print(" el cociente  de 10/4 es : ",10//4)
print(" el exponente de 10^4 es :", 10**4)
#resolver la ecuación cuadrática 2x^2-7x+3=0
a=2
b= -7
c= 3
x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b- (b**2-4*a*c)**0.5)/(2*a)
print( "la respuesta es ", x1 )
print("la respuesta es ", x2 )
#operaciones con cadena de texto
print("SNPP "+"CTFPPJ "+"PROGRAMACIÓN PYTHON")
print("aula "+str(2102))
#operaciones mixta
print("tun chi"*5)
print("Ja"*(2**3))
#operacion de comparacion 
print(3>4)
print(3<4)
print(3>=4)
print(4<=4)
print(3==4)
print(3!=4)
#operaciones con cadenas 
print("Python">"Pytho")
print("aaaa" >="abaaa")
print( len("aaaa") >= len("abaa"))
print ("python" !="PYTHON")
#OPERACIONES LÓGICOS
print(10 >4 and "Z"<"A")
print(10 >4 or "Z "> "A")
print(not(10<4)and "Z">"A")