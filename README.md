# Sistema de Gestión de Estudiantes y Calificaciones

## Descripción

El **Sistema de Gestión de Estudiantes y Calificaciones** es una aplicación interactiva que permite gestionar la información de los estudiantes, registrar sus calificaciones, calcular su promedio y realizar consultas. La aplicación permite agregar estudiantes, ingresar y actualizar calificaciones, consultar promedios, y eliminar estudiantes de la base de datos.

Este sistema es una herramienta sencilla para gestionar a los estudiantes y sus calificaciones, y fue diseñado para facilitar la administración de datos académicos en entornos educativos.

## Funcionalidades

El sistema permite realizar las siguientes operaciones:

1. **Agregar Estudiante**: El usuario puede ingresar los detalles de un nuevo estudiante (DNI, nombre, apellido, edad) para agregarlo a la lista de estudiantes registrados.
2. **Ingresar Calificación**: Se puede ingresar una nueva calificación para un estudiante ya registrado. Las calificaciones deben estar en un rango de 0 a 100.
3. **Consultar Estudiantes**: Permite ver la información de un estudiante, incluyendo su DNI, nombre, apellido, edad, las calificaciones ingresadas y su promedio de calificaciones.
4. **Eliminar Estudiante**: Permite eliminar un estudiante de la lista registrada.
5. **Acerca de**: Muestra información sobre el equipo de desarrollo, roles, y el eslogan del proyecto.
6. **Salir**: Termina la ejecución del programa.

# Estructura del Proyecto

El proyecto se compone de varios archivos que cumplen con las siguientes funciones:

## Archivos

- **Estudiante.py**: Contiene la clase **Estudiante**, que define los atributos y métodos para gestionar la información del estudiante, como su DNI, nombre, apellido, edad y calificaciones. Además, esta clase tiene métodos para calcular el promedio de las calificaciones y agregar nuevas calificaciones.

- **GestorEstudiante.py**: Contiene la clase **GestorEstudiante**, que administra la lista de estudiantes. Esta clase permite agregar estudiantes, ingresar calificaciones, consultar los datos de los estudiantes y eliminar registros.

- **main.py**: Es el archivo principal que ejecuta el programa. Muestra un menú de opciones para que el usuario pueda interactuar con el sistema. El programa permite ingresar estudiantes, agregar calificaciones, consultar estudiantes y sus promedios, eliminar estudiantes y ver la ficha técnica del equipo.

---

## Descripción de las Clases

### Clase Estudiante

La clase **Estudiante** tiene los siguientes atributos y métodos:

**Atributos:**
- `dni`: El DNI del estudiante.
- `nombre`: El nombre del estudiante.
- `apellido`: El apellido del estudiante.
- `edad`: La edad del estudiante.
- `notas`: Una lista que contiene las calificaciones del estudiante.

**Métodos:**
- `__init__(dni, nombre, apellido, edad)`: Constructor que inicializa un nuevo objeto Estudiante con los atributos proporcionados.
- `__str__()`: Método que devuelve una cadena representativa del objeto, mostrando sus atributos.
- `calcular_promedio()`: Calcula y devuelve el promedio de las calificaciones del estudiante. Si no tiene calificaciones, imprime un mensaje de advertencia.
- `agregar_nota(nueva_nota)`: Permite agregar una nueva calificación al estudiante, validando que esté entre 0 y 100.
- `set_nombre(nombre)` y `get_nombre()`: Métodos para establecer y obtener el nombre del estudiante.
- `set_edad(edad)` y `get_edad()`: Métodos para establecer y obtener la edad del estudiante, validando que la edad sea positiva.

### Clase GestorEstudiante

La clase **GestorEstudiante** administra la lista de estudiantes registrados y tiene los siguientes métodos:

**Atributos:**
- `lista_estudiantes`: Lista que almacena los objetos Estudiante registrados.

**Métodos:**
- `agregar_estudiante()`: Solicita al usuario que ingrese los datos de un nuevo estudiante y lo agrega a la lista de estudiantes.
- `ingresar_calificaciones()`: Permite ingresar una calificación para un estudiante ya registrado. El usuario selecciona el estudiante por su índice.
- `consultar_estudiantes()`: Muestra los datos de los estudiantes registrados, junto con sus calificaciones y promedio.
- `eliminar_estudiante()`: Elimina un estudiante de la lista de estudiantes.
- `_validar_lista_vacia()`: Método auxiliar que valida si la lista de estudiantes está vacía.
- `_validar_indice(indice)`: Método auxiliar que valida si el índice ingresado por el usuario es válido.

---

## Interfaz de Usuario (main.py)

El archivo **main.py** es el que se ejecuta directamente. Proporciona un menú interactivo en la línea de comandos que permite al usuario seleccionar una opción de las disponibles:

1. Agregar un estudiante.
2. Ingresar una calificación para un estudiante.
3. Consultar la información de un estudiante.
4. Eliminar un estudiante.
5. Ver la ficha técnica del equipo.
6. Salir del programa.

---

## Contribuyentes

- **Juan David Guzman**: Scrum Master
- **Giovana Orejarena**: Product Owner
- **Josue Bustamante**: Developer
- **Jhan Albarracin**: Developer

**Eslogan**: Más que código, creamos experiencias.


## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación utilizado para desarrollar la aplicación.
- **Interfaz de línea de comandos (CLI)**: El sistema interactúa con el usuario a través de un menú basado en texto.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalada la versión 3.x de **Python** en tu sistema. Si aún no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
