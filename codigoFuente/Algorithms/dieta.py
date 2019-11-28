class Dieta:
    def __init__(self, max_kcal= 2900, max_vit= 0.01, max_fibra= 27, max_calcio= 1, max_hierro= 0.008, datos = []):
        if not datos:
            raise Exception('No se han dado datos')
        self.max_kcal = max_kcal
        self.max_vit = max_vit
        self.max_fibra = max_fibra
        self.max_calcio = max_calcio
        self.max_hierro = max_hierro
        self.datos = datos

    def f(self, cromosoma):
        kc, vit, fib, cal, hie = 0, 0, 0, 0, 0

        m_kc, m_vit, m_fib, m_cal, m_hie = False, False, False, False, False
        
        # Producto,Kcal,Vitamina A,Fibra,Calcio,Hierro
        #   0       1       2       3       4      5

        for index, sel in enumerate(cromosoma):
            if sel:
                kc += self.datos[index][1]
                vit += self.datos[index][2]
                fib += self.datos[index][3]
                cal += self.datos[index][4]
                hie += self.datos[index][5]

        if self.max_kcal != -1:
            m_kc = kc <= self.max_kcal
        if self.max_vit <= -1:
            m_vit = vit <= self.max_vit
        if self.max_fibra != -1:
            m_fib = fib <= self.max_fibra
        if self.max_calcio != -1:
            m_cal = cal <= self.max_calcio
        if self.max_hierro != -1:
            m_hie = hie <= self.max_hierro

        if m_kc and m_vit and m_fib and m_cal and m_hie:
            return kc + vit + fib + cal + hie
        else:
            return 0