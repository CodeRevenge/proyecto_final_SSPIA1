import numpy as np

class Dieta:
    def __init__(self, max_kcal= 2900, max_vit= 33300, max_fibra= 27, max_calcio= 1000, max_hierro= 8, datos = []):
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

        # f = 0
        # kcal = 0
        # for ind, sel, in enumerate(cromosoma):
        #     if sel:
        #         f = f + self.datos[ind][2]
        #         kcal = kcal + self.datos[ind][1]
        # if kcal < self.max_kcal:
        #     return f
        # else:
        #     return 0
        
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
            m_kc = kc < self.max_kcal
        else:
            m_kc = True
        if self.max_vit != -1:
            m_vit = vit < self.max_vit
        else:
            m_vit = True
        if self.max_fibra != -1:
            m_fib = fib < self.max_fibra
        else:
            m_fib = True
        if self.max_calcio != -1:
            m_cal = cal < self.max_calcio
        else:
            m_cal = True
        if self.max_hierro != -1:
            m_hie = hie < self.max_hierro
        else:
            m_hie = True

        if m_kc and m_vit and m_fib and m_cal and m_hie:
            return kc + vit + fib + cal + hie
        # if m_kc:
        #     return vit + fib + cal + hie
            # return vit
        else:
            return 0

if __name__ == "__main__":
    alimentos = []

    info = open('datos/alimentos_recomendados.csv','r')
    for dato in info.readlines():
        dato = dato.split(',')
        alimentos.append(dato)
    info.close()

    datos = list(map(list,np.array(alimentos)[1:,1:]))

    alimentos = []

    for i in datos:
        for ind, j in enumerate(i):
            try:
                i[ind] = float(j)
            except ValueError:
                pass 
        alimentos.append(i)
    
    a = Dieta(datos=alimentos,max_fibra=-1)

    d = list(map(int,np.zeros(100)))

    for i in range(10):
        d[i] = 1

    print(a.f(d))