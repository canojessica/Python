agenda ={}

def cargar_agenda(nombre, telefono):
    agenda[nombre ]= telefono 

def ver_agenda():
    print(agenda)


def ver_agenda_detalle():
    print("lista de contactos")
    for nombre, tel in agenda.items():
        print(f"{nombre}:{tel}")


if __name__ =="__main__" :
  cargar_agenda("jessica", "0971871696")
  cargar_agenda("leticia","0987654321")
  ver_agenda()
  ver_agenda_detalle()