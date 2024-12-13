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
    
    def agregar_nota(self, nueva_nota):
        """
        Agrega una nueva calificación a la lista de notas del estudiante.

        Args:
            nueva_nota (float): Calificación a agregar (debe estar entre 0 y 100).
        """
        if 0 <= nueva_nota <= 100:
            self.notas.append(nueva_nota)
            print(f"La nota {nueva_nota} fue agregada correctamente.")
        else:
            print("Error: la nota debe estar entre 0 y 100.")
    
    def set_nombre(self, nombre):
        """
        Modifica el nombre del estudiante.

        Args:
            nombre (str): Nuevo nombre del estudiante.
        """
        self.nombre = nombre

    def get_nombre(self):
        """
        Devuelve el nombre del estudiante.

        Returns:
            str: Nombre del estudiante.
        """
        return self.nombre

    def set_edad(self, edad):
        """
        Modifica la edad del estudiante si es válida.

        Args:
            edad (int): Nueva edad del estudiante (debe ser positiva).
        """
        if edad > 0:
            self.edad = edad
        else:
            print("Error: la edad debe ser un número positivo.")

    def get_edad(self):
        """
        Devuelve la edad del estudiante.

        Returns:
            int: Edad del estudiante.
        """
        return self.edad

