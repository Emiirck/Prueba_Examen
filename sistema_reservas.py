
Ruser = {}


def main():
    while True: 
        print("\nMenú de Opciones")
        print("1. Registrar Usuario")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Actualizar producto")
        print("5. Salir")
        opcion = input("Elige una opción: ")


def Ruser():
    
    print("Bienvenido al Sistema de registro de cuenta de la agencia de viajes" )
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = (input("Ingrese una contraseña: "))
    ccontraseña = (input("Ingrese nuevamente la contraseña: "))
    if contraseña == ccontraseña:  
        print("Usuario " + usuario, "registrado con éxito!")
    else:
        print("Las contraseñas no coinciden, por favor vuelva a intentarlo\n")
    
    return main

    
    
Ruser()
    
    
    
    
    
    
    


Ruser()