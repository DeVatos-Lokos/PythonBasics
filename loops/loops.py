class NaturalNumbers:
    def __init__(self):
        pass

    def get_first_n_for(self, n): # Ejemplo
        """
        Obtener los primeros n naturales en una lista con for
        """
        first_n = [] # Se declara una lista donde almacenaremos los numeros
        for i in range(n): # Se itera sobre range que genera un rango de 0 a n
            first_n.append(i) # Almacenamos la variable del ciclo en la lista con append 
        print("FIRST n (n={}) FOR: {}".format(n, first_n))
        return first_n # Regresamos la lista

    def get_first_n_while(self, n): # Ejemplo
        """
        Obtener los primeros n naturales en una lista con while
        """
        first_n = [] # Se declara una lista donde almacenaremos los numeros
        n_count = 0 # Inicializamos un contador para saber en que iteracion vamos dentro del ciclo
        while n_count < n: # Condición de terminación del ciclo 
            first_n.append(n_count) # ALmacenamos el contador (contablizador del ciclo) en la lista
            n_count += 1 # Sumamos uno al contador puesto que termina ek ciclo, si no nunca n_count será mayor o igual que n y tendremos un loop infinito
        print(f"FIRST n (n={n}) WHILE: {first_n}")
        return first_n

    def get_first_n_pair_for(self, n): # Ejercicio
        """
        Obtener los primeros n pares en una lista con for
        """
        return []

    def get_first_n_pair_while(self, n): # Ejercicio
        """
        Obtener los primeros n pares en una lista con while
        """
        return []

    def get_factorial_for(self, n): # Ejercicio
        """
        Obtener el factorial de n con for, regresa un int
        """
        return 0

    def get_factorial_while(self, n): # Ejercicio
        """
        Obtener el factorial de n con while, regresa un int
        """
        return 0

    def get_factorial_recursive(self, n): #Ejemplo
        """
        Obtener el factorial de n recursivamente, regresa un int
        """
        if n <= 1:
            return 1
        return n * self.get_factorial_recursive(n-1)

    def get_n_pow_2_for(self, n): # Ejemplo
        """
        Obtener el cuadrado de los primeros n con for, regresa una lista
        """
        n_pow_2 = []
        for i in range(n):
            n_pow_2.append(
                i ** 2
            )
        print(f"FIRST n (n={n}) POW 2: {n_pow_2}")
        return n_pow_2

    def get_n_pow_2_while(self, n): # Ejercicio
        """
        Obtener el cuadrado de los primeros n con while, regresa una lista
        """
        return []

    def get_n_sum_recursive(self, n): #Ejemplo
        """
        Obtener la suma de los primeros n recursivamente, regresa un int
        """
        if n <= 0:
            return 0
        return n + self.get_n_sum_recursive(n-1)

    def get_n_sum_for(self, n): # Ejercicio
        """
        Obtener la suma de los primeros n con for, regresa un int
        """
        return 0

    def get_n_sum_while(self, n): # Ejercicio
        """
        Obtener la suma de los primeros n con while, regresa un int
        """
        return 0