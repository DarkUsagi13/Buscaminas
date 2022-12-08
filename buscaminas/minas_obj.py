import random
import time


class Tablero:
    def __init__(self, numfilas=1, numcolumnas=1, numminas=1):
        self.numfilas = numfilas
        self.numcolumnas = numcolumnas
        self.numminas = numminas

    def filas(self):
        return range(self.numfilas)

    def columnas(self):
        return range(self.numcolumnas)

    def minas(self):
        return range(self.numminas)

    def coordenadas(self):
        listaminas = set()
        random.seed(time.time())
        while len(listaminas) < self.numminas:
            c_fila = random.randint(0, self.numfilas - 1)
            c_columna = random.randint(0, self.numcolumnas - 1)
            coordenada = (c_fila, c_columna)
            listaminas.add(coordenada)
        return listaminas