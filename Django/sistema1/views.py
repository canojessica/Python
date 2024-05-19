from django.http import HttpResponse
from  django.shortcuts import redirect 


def saludo (request):
    return HttpResponse("Hola mundo ")

def get_google (request):
    url="https:www.google.com.py"
    return redirect (url)
 
def fibo (request):
    lista=[]
    for i in range (100+1):
        lista.append(i)
    return HttpResponse(f'{lista}')

def show(request):
    text = ("En un jardín muy risueño y soleado,\n"
        "las flores bailan al ritmo animado,\n"
        "el sol les canta con su luz dorada,\n"
        "y hasta el viento se une a la algarabía.\n"
        "Las mariposas revolotean contentas,\n"
        "mientras las abejas hacen acrobacias ligeras,\n"
        "los pájaros entonan su canción alegre,\n"
        "y el arcoíris pinta el cielo con sus colores."
        "(•ㅅ•)")
    return HttpResponse(text)