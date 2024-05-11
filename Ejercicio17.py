#funciones matemáticas
def suma( a, b ):
    return a + b

def resta( a, b ):
    return a-b

def multiplicacion( a, b ): 
    return a*b

def division( a , b ):
  if(b == 0 ):
        return "No se  puede deividir por CERO "
  else:
      return a/b
  
def raiz(a,b =2 ):
    return a**(1/b)

#cuando ejecutamos el script, _name_ para a ser igual
if  __name__ == '__main__':
    print("La suma de 3 y 4 son " , suma(3,4))
    print("la resta de 3 y 4 son ", resta(3,4))   
    print("la multiplicacion de 3 y 4 son ", multiplicacion(3,4))
    print("la divicion de 3 y 4 son ", division(3,4))
    print( "la raiz de 3 y 4 son" , raiz(3,4))