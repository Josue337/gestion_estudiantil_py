import estudiante as estu

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
        
    def _validar_lista_vacia(self):
        """
        Valida si la lista de estudiantes está vacía.

        Returns:
            bool: True si la lista tiene estudiantes, False si está vacía.
        """
        if not self.lista_estudiantes:
            print("No hay estudiantes registrados. Por favor, agregue estudiantes primero.")
            return False
        return True
    
    def _validar_indice(self, indice):
        """
        Valida si el índice proporcionado está dentro del rango de la lista de estudiantes.

        Args:
            indice (int): Índice a validar.

        Returns:
            bool: True si el índice es válido, False en caso contrario.
        """
        if 1 <= indice <= len(self.lista_estudiantes):
            return True
        print("Índice fuera de rango. Por favor, intente nuevamente.")
        return False
    
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
                
    def ingresar_calificaciones(self):
        """
        Permite ingresar calificaciones para un estudiante existente en la lista.
        """
        print("---------------------")
        print("INGRESAR CALIFICACIONES")
        print("---------------------\n")

        if not self._validar_lista_vacia():
            return

        for i, estudiante in enumerate(self.lista_estudiantes, start=1):
            print(f"{i}. {estudiante.get_nombre()}")

        try:
            indice = int(input("Seleccione el índice del estudiante: "))
            if not self._validar_indice(indice):
                return

            nota_nueva = float(input("Ingrese la nueva nota: "))
            if 0 <= nota_nueva <= 100:
                estudiante_seleccionado = self.lista_estudiantes[indice - 1]
                estudiante_seleccionado.agregar_nota(nota_nueva)
            else:
                print("Error: La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
        except Exception as ex:
            print(f"Error inesperado: {ex}.")
                
    def consultar_estudiantes(self):
        """
        Muestra información detallada de un estudiante seleccionado de la lista.
        """
        if not self._validar_lista_vacia():
            return

        print("---------------------")
        print("CONSULTAR ESTUDIANTE")
        print("---------------------\n")

        for i, estudiante in enumerate(self.lista_estudiantes, start=1):
            print(f"{i}. {estudiante.get_nombre()}")

        try:
            indice = int(input("Seleccione el número del estudiante a consultar: "))
            if not self._validar_indice(indice):
                return

            estudiante_seleccionado = self.lista_estudiantes[indice - 1]
            print(f"""
            DNI: {estudiante_seleccionado.dni}
            Nombre: {estudiante_seleccionado.nombre}
            Apellido: {estudiante_seleccionado.apellido}
            Edad: {estudiante_seleccionado.edad}
            Notas: {estudiante_seleccionado.notas}
            Promedio: {estu.Estudiante.calcular_promedio(estudiante_seleccionado)}
            """)
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
        except Exception as ex:
            print(f"Error inesperado: {ex}.")