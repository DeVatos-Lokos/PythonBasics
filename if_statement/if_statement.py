# En esta práctica verémos el condicional if,
# que permite dirigir el flujo del código
# en función de una condición de evaluación,
# el simil en español es el si
# p. ej si (if) llovio, no tiendo la ropa, si no (else) llovió sí la tiendo

class Ropa:
    def __init__(self):
        pass

    def tender(self, clima): # Ejemplo
        if clima == "lluvia":
            return "no tiendo"
        else:
            return "tiendo"

    def tender_con_negacion(self, clima): # Ejemplo
        """
        Este ejemplo es equivalente (esto quiere decir que para
        la misma entrada dará el mismo resultado) a la función
        tender, solo que usamos la negación != que significa 
        es distinto de, contrario a == que significa que es igual a
        """
        if clima != "lluvia":
            return "tiendo" # El return corta el flujo ya no se ocupa else
        return "no tiendo"

        # En al función de arriba siempre que clima sea distinto de lluvia
        # vas a tender la ropa y regresaras el resultado "tiendo", el return
        # corta el flujo por lo que la linea 26 (return no tiendo) nunca se 
        # ejecutará si clima es distinto de lluvia y la 25 sí, en cambio, 
        # si clima es lluvia la 25 no se ejefcutará y continuara el flujo
        # en la línea 26


class Semaforo:
    def __init__(self):
        pass

    def avanza(self, color):
        """
        Debe regresar "avanza" si el color es verde, y "no avanza" si es amarillo o rojo
        """
        pass

class Pastel:
    def __init__(self):
        pass

    def suficiente(self, cantidad_rebanadas, cantidad_comensales):
        """
        Debe regresar "suficiente" si cantidad_rebanadas es mayor o 
        igual que la cantidad de comensales, si es menor regresará
        "insuficiente"
        """
        pass

    def diferencia(self, cantidad_rebanadas, cantidad_comensales):
        """
        Debe regresar el valor absoluto de la diferencia entre cantidad_rebanadas
        y cantidad_comensales
        """
        pass

    def es_de_chocolate(self, sabor):
        """
        Debe regresar "si" si el sabor es "chocolate", "no" si no lo es
        """
        pass

class Futbol:
    def __init__(self):
        pass

    def equipo_valido(self, cantidad_jugadores):
        """
        Debe regresar "valido" si tiene 11 jugadores,
        de lo contrario regresara no valido
        """
        pass
