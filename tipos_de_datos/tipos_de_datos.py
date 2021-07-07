# En esta practica entendéremos los tipos de datos básicos en python, y realizaremos
# algunas de sus operaciones básicas

####################################################################################
####################################################################################
#########TODO LO QUE COMIENZE CON # O ESTÉ ENTRE """""" ES UN COMENTARIO############
###########PYTHON NO LO ITERPRETARÁ CÓMO CÓDIGO, SOLO SON EXPLICACIONES#############
####################################################################################
####################################################################################


class TiposDeDatos:
    def __init__(self):
        # Revisa el ejemplo de es boolean y utiliza las variables declaradas abajo
        # para resolver los ejercicios
        self.tipo_string = ""
        self.tipo_bool = False
        self.tipo_int = 0
        self.tipo_float = 0.0
        self.tipo_byte = b''
        self.tipo_list = []

    def es_string(self, recibimos): #Ejemplo
        """
        El tipo de dato string, es una cadena de carácteres, como una palabra o una letra,
        se expresa con "" comillas, otros tipos de datos puede convertirse en string, como un número,
        bastara expresarlo con comillas, p. ej "1".
        Este método recibe parámetro s, regresa verdadero si es de tipo string o falso si no lo es

        """
        # Para saber el tipo de un dato es necesario invocar el método type
        # Un método no necesariamente debe retornar (return) algo, pero es muy útil
        # saber usar return, en español la línea de abajo se leería de la sig manera
        # Retorna si el tipo de dato que recibimos es igual al tipo de dato de self.tipo string que es string
        # Si son iguales == es verdadero, si no es falso, regresamos True o False
        return type(self.tipo_string) == type(recibimos)


    def es_boolean(self, recibimos): #Ejemplo
        """
        El tipo boolean puede ser vedadero (True) o falso (False), este méetodo,
        nos regresará True si es boolean y false, si no lo es
        """
        return type(self.tipo_bool) == type(recibimos) 

    def es_int(self, recibimos): # Ejercicio
        """
        EL tipo de dato int, es un número entero, puede ser negativo o positivo
        """
        return type(self.tipo_int) == type(recibimos)

    def es_float(self, recibimos): # Ejercicio
        """
        El tipo de dato float es un número décimal
        """
        return type(self.tipo_float) == type(recibimos)

    def es_byte(self, recibimos): # Ejercicio
        """
        El tipo de dato byte es una cadena de bytes, es el tipo más básico en cualquier lenguaje de programación,
        todos los demás tipos de datos pueden transformarse en este
        """
        return type(self.tipo_byte) == type(recibimos)

    def es_list(self, recibimos):
        """
        El tipo de dato lista, es un arreglo que puede contener otros tipos de datos, 
        una lista de objetos (Sting, List, Tuple, Clases) o tipos primitivos (int, byte, float).
        Es una estructura de datos, la más básica de todas y probablemente la que más usaran,
        en python un String es, d hecho una lista de carácteres.
        """
        return type(self.tipo_list) == type(recibimos)

    # DECLARACIÓN DE VARIABLES Y ASIGNACIONES
    def regresa_un_string(self): # Ejemplo
        return "Hola mundo"

    def regresa_un_boolean(self):
        return True

    def regresa_un_int(self):
        return 1

    def regresa_un_float(self):
        return 1.0

    def regresa_un_byte(self):
        return b""

    def regresa_una_lista(self):
        return []

    def regresa_una_lista_de_longitud_10(self):
        return [i for i in range(10)]

    # CONVERSIONES DE DATOS
    def to_string(self, recibimos): #Ejemplo
        """
        Es una de las conversiones (casting en inglés) más comunes, consiste en generar la
        representación en cádena de texto de un objeto, en python todo es un objeto, es el tipo
        básico en los lenguajes con orientación a objetos, lo verémos más adelante.
        El método __str__ que se llama con str() es el encargado de hacer dicho proceso por default
        en python
        """
        return str(recibimos)

    def int_to_float(self, recibimos):
        """
        La conversión de un entero a float solo agrega decimales al entero, 0 se convierte en 0.0,
        1 en 1.0 y así sucesivamente
        """
        return float(recibimos)

    def float_to_int(self, recibimos):
        """
        La conversión de float a entero le quita decimales, se pierde información, un 3.9, se convierte en 3,
        3.1 en 3.
        """
        return int(recibimos)