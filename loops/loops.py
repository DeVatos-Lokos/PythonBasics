class NaturalNumbers:
    def __init__(self):
        pass

    def get_first_n_for(self, n): # Ejemplo
        first_n = []
        for i in range(n):
            first_n.append(i)
        print("FIRST n (n={}) FOR: {}".format(n, first_n))
        return first_n

    def get_first_n_while(self, n): # Ejemplo
        first_n = []
        n_count = 0
        while n_count < n:
            first_n.append(n_count)
            n_count += 1
        print(f"FIRST n (n={n}) WHILE: {first_n}")
        return first_n

    def get_first_n_pair_for(self, n):
        return [i for i in range(0, n, 2)]

    def get_first_n_pair_while(self, n):
        return [i for i in range(0, n, 2)]

    def get_factorial_for(self, n):
        return self.get_factorial_recursive(n)

    def get_factorial_while(self, n):
        return self.get_factorial_recursive(n)

    def get_factorial_recursive(self, n): #Ejemplo
        if n <= 1:
            return 1
        return n * self.get_factorial_recursive(n-1)

    def get_n_pow_2_for(self, n):
        n_pow_2 = []
        for i in range(n):
            n_pow_2.append(
                i ** 2
            )
        print(f"FIRST n (n={n}) POW 2: {n_pow_2}")
        return n_pow_2

    def get_n_pow_2_while(self, n):
        return self.get_n_pow_2_for(n)

    def get_n_sum_recursive(self, n): #Ejemplo
        if n <= 0:
            return 0
        return n + self.get_n_sum_recursive(n-1)

    def get_n_sum_for(self, n):
        return self.get_n_sum_recursive(n)

    def get_n_sum_while(self, n):
        return self.get_n_sum_recursive(n)