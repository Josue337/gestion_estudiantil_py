class GestorEstudiante:
    
    """
    Clase para gestionar un conjunto de estudiantes, incluyendo funcionalidades para agregar, consultar,
    modificar y eliminar estudiantes, así como administrar sus calificaciones.

    Atributos:
        lista_estudiantes (list): Lista que almacena objetos de tipo Estudiante.

    Métodos:
        _validar_lista_vacia: Verifica si la lista de estudiantes está vacía.
        _validar_indice: Verifica si un índice proporcionado es válido.
        agregar_estudiante: Agrega un nuevo estudiante al sistema.
        ingresar_calificaciones: Permite registrar calificaciones para un estudiante.
        consultar_estudiantes: Muestra los detalles de un estudiante específico.
        eliminar_estudiante: Elimina un estudiante del sistema.
    """

    def __init__(self):
        """
        Constructor de la clase GestorEstudiante.
        Inicializa una lista vacía para almacenar objetos de tipo Estudiante.
        """
        self.lista_estudiantes = []
    
    def agregar_estudiante(self):
            """
            Permite agregar un nuevo estudiante al sistema solicitando su información básica.
            """
            print("---------------------")
            print("AGREGAR ESTUDIANTE")
            print("---------------------\n")

            try:
                dni = int(input("Ingrese el DNI del estudiante: "))
                nombre = input("Ingrese el nombre del estudiante: ")
                apellido = input("Ingrese el apellido del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))

                if edad < 0:
                    print("Error: La edad no puede ser negativa.")
                    return

                estudiante = estu.Estudiante(dni, nombre, apellido, edad)
                self.lista_estudiantes.append(estudiante)
                print(f"Estudiante {nombre} {apellido} agregado correctamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos donde corresponda.")
            except Exception as ex:
                print(f"Error inesperado: {ex}.")