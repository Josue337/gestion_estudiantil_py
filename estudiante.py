class Estudiante:
    """
    Clase que representa a un estudiante, permitiendo gestionar su información personal y sus notas académicas.

    Atributos:
        dni (str): Documento de identidad del estudiante.
        nombre (str): Nombre del estudiante.
        apellido (str): Apellido del estudiante.
        edad (int): Edad del estudiante.
        notas (list): Lista de calificaciones asociadas al estudiante.

    Métodos:
        __init__: Inicializa un nuevo estudiante con los atributos básicos.
        __str__: Devuelve una representación en cadena del estudiante.
        calcular_promedio: Calcula y retorna el promedio de las calificaciones del estudiante.
        agregar_nota: Agrega una calificación a la lista de notas del estudiante.
        set_nombre: Permite modificar el nombre del estudiante.
        get_nombre: Devuelve el nombre del estudiante.
        set_edad: Permite modificar la edad del estudiante.
        get_edad: Devuelve la edad del estudiante.
    """

    def __init__(self, dni, nombre, apellido, edad):
        """
        Constructor de la clase Estudiante.

        Args:
            dni (str): Documento de identidad del estudiante.
            nombre (str): Nombre del estudiante.
            apellido (str): Apellido del estudiante.
            edad (int): Edad del estudiante.
        """
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = []  # Lista vacía para almacenar las calificaciones.

    def __str__(self):
        """
        Devuelve una representación en cadena del estudiante.

        Returns:
            str: Representación en cadena del estudiante.
        """
        return f"Estudiante(dni={self.dni}, nombre={self.nombre}, apellido={self.apellido}, edad={self.edad}, notas={self.notas})"
    
    
    def calcular_promedio(self):
        """
        Calcula y muestra el promedio de las notas del estudiante.

        Returns:
            float: Promedio de las calificaciones, si existen; None en caso contrario.
        """
        if not self.notas:
            print("No hay notas disponibles para calcular el promedio.")
            return None
        promedio = sum(self.notas) / len(self.notas)
        print(f"El promedio del estudiante {self.nombre} {self.apellido} es de {promedio:.2f}.")
        return promedio
