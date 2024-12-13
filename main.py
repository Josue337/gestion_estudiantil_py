import gestor_estudiante as ge

def acerca_de():
    """
    Muestra información acerca del equipo que desarrolló el programa, incluyendo los integrantes,
    roles y el eslogan del proyecto.
    """
    print("---------------------")
    print("INTEGRANTES")
    print("---------------------\n")
    print("Josue Bustamante")
    print("Juan David Guzman")
    print("Jhan Albarracin")
    print("Giovana Orejarena")
    print("---------------------")
    print("ROLES")
    print("---------------------\n")
    print("Juan David Guzman: Scrum Master")
    print("Giovana Orejarena: Product Owner")
    print("Josue Bustamante: Developer")
    print("Jhan Albarracin: Developer")
    print("---------------------")
    print("ESLOGAN")
    print("---------------------\n")
    print("Más que código, creamos experiencias.\n")

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles para el usuario.
    """
    print("<--------------------->")
    print("GESTOR ESTUDIANTES")
    print("<--------------------->\n")
    print("1. Ingresar estudiante")
    print("2. Ingresar nota")
    print("3. Consultar estudiante")
    print("4. Eliminar estudiante")
    print("5. Acerca de")
    print("6. Salir del programa\n")

def ejecutar_opcion(opcion, gestor):
    """
    Ejecuta la opción seleccionada por el usuario.

    Args:
        opcion (int): Opción seleccionada por el usuario.
        gestor (GestorEstudiante): Instancia del gestor que administra los estudiantes.

    Returns:
        bool: False si el usuario selecciona la opción de salir (6), True en caso contrario.
    """
    opciones = {
        1: gestor.agregar_estudiante,
        2: gestor.ingresar_calificaciones,
        3: gestor.consultar_estudiantes,
        4: gestor.eliminar_estudiante,
        5: acerca_de
    }

    if opcion in opciones:
        opciones[opcion]()  # Llama a la función correspondiente.
    elif opcion == 6:
        print("Has salido del programa.")
        return False
    else:
        print("Ingrese una opción dentro del rango dado.")
    return True

if __name__ == '__main__':
    """
    Punto de entrada principal del programa.
    Crea una instancia de GestorEstudiante y permite al usuario interactuar con el menú principal.
    """
    gestor = ge.GestorEstudiante()  # Instancia del gestor de estudiantes.

    while True:
        try:
            mostrar_menu()  # Muestra el menú de opciones.
            opcion = int(input("Ingrese la opción deseada: "))
            if not ejecutar_opcion(opcion, gestor):  # Ejecuta la opción seleccionada.
                break
        except ValueError:
            print("Error: Ingrese un número válido.")
        except Exception as ex:
            print(f"Error inesperado: {ex}")
