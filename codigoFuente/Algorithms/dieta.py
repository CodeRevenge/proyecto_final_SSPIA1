class Dieta:
    def __init__(self, max_kcal= 2900, max_vit= 0.01, max_fibra= 27, max_calcio= 1, max_hierro= 0.008, datos = []):
        if not datos:
            raise Exception('No se han dado datos')
        self.max_kcal = max_kcal
        self.max_vit = max_vit
        self.max_fibra = max_fibra
        self.max_calcio = max_calcio
        self.max_hierro = max_hierro

    def f(self, cromosoma):
        f = 0
        kc = 0
        vit = 0
        fib = 0
        cal = 0
        hie = 0

        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f = f + self._

        # f = 0
        # peso = 0
        # for i in range(len(cromosoma)):
        #     if cromosoma[i]:
        #         f = f + self._valores[i]
        #         peso = peso + self._pesos[i]
        # if peso < self._capacidad:
        #     return f
        # else:
        #     return 0
        pass
