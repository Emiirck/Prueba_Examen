
usuarios = []
reservas = []

def registrar_usuario():
    while True:
        nombre_usuario = input("Ingresa el nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("Este nombre de usuario ya está registrado. Por favor, elige otro.")
        else:
            usuarios.append(nombre_usuario)
            print(f"Usuario {nombre_usuario} registrado con éxito.")
            break

def verificar_usuario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    if nombre_usuario in usuarios:
        return nombre_usuario
    else:
        print("Usuario no encontrado. ¿Deseas registrarte?")
        respuesta = input("Escribe 'sí' para registrarte o 'no' para intentar nuevamente: ").lower()
        if respuesta == 'sí':
            registrar_usuario()
            return usuarios[-1]
        else:
            return None

def reservar_viaje():
    nombre_usuario = verificar_usuario()
    if nombre_usuario:
        destino = input("Ingresa el destino del viaje: ")
        fecha = input("Ingresa la fecha del viaje (DD/MM/AAAA): ")
        reserva = {'usuario': nombre_usuario, 'destino': destino, 'fecha': fecha}
        reservas.append(reserva)
        print(f"Reserva para {nombre_usuario} al destino {destino} en la fecha {fecha} realizada con éxito.")

def ver_reservas():
    nombre_usuario = verificar_usuario()
    if nombre_usuario:
        usuario_reservas = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
        if usuario_reservas:
            print(f"Reservas de {nombre_usuario}:")
            for i, reserva in enumerate(usuario_reservas, start=1):
                print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
        else:
            print("No tienes reservas registradas.")

def cancelar_reserva():
    nombre_usuario = verificar_usuario()
    if nombre_usuario:
        usuario_reservas = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
        if usuario_reservas:
            print(f"Reservas de {nombre_usuario}:")
            for i, reserva in enumerate(usuario_reservas, start=1):
                print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
            indice = int(input("Ingresa el número de la reserva que deseas cancelar: ")) - 1
            if 0 <= indice < len(usuario_reservas):
                reservas.remove(usuario_reservas[indice])
                print("Reserva cancelada con éxito.")
            else:
                print("Número de reserva no válido.")
        else:
            print("No tienes reservas registradas.")

def menu():
    while True:
        print("\nBienvenido al Sistema de Reservas")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print("Gracias por usar el Sistema de Reservas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor elige nuevamente.")

menu()
