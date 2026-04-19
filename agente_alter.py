from entorno import Agente

class AgenteAlter(Agente):
    """
    Agente Basado en Utilidad con distancia Manhattan.
    Utilidad = -distancia_manhattan (menos pasos = mayor utilidad)
    """

    def __init__(self, filas=10, columnas=10):
        super().__init__(nombre="Agente Basado en Utilidad")
        self.filas = filas
        self.columnas = columnas
        self.meta = (filas - 1, columnas - 1)
        self.visitados = set()
        self.ultima_posicion = None

    def al_iniciar(self):
        self.visitados.clear()
        self.ultima_posicion = None

    def _distancia_manhattan(self, pos):
        r, c = pos
        mr, mc = self.meta
        return abs(mr - r) + abs(mc - c)

    def decidir(self, percepcion):
        pos_actual = percepcion['posicion']
        vertical, horizontal = percepcion["direccion_meta"]

        self.visitados.add(pos_actual)

        utilidad = {'arriba': 0, 'abajo': 0, 'izquierda': 0, 'derecha': 0}

        for direccion in self.ACCIONES:
            estado = percepcion[direccion]
            dr, dc = self.DELTAS[direccion]
            r, c = pos_actual
            nueva_posicion = (r + dr, c + dc)

            if estado == 'pared' or estado is None:
                utilidad[direccion] = -10000
                continue

            if estado == 'meta':
                utilidad[direccion] = 10000
                continue

            # Utilidad = -distancia Manhattan (real)
            utilidad[direccion] = -self._distancia_manhattan(nueva_posicion)

            if nueva_posicion in self.visitados:
                utilidad[direccion] -= 5
            if nueva_posicion == self.ultima_posicion:
                utilidad[direccion] -= 10

        mejor_accion = max(utilidad, key=utilidad.get)
        self.ultima_posicion = pos_actual

        return mejor_accion