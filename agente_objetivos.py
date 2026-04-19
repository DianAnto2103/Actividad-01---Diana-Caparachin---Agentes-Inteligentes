from entorno import Agente


class AgenteBObjetivos(Agente):

    def __init__(self, nombre="Agente Basado en Objetivos"):
        super().__init__(nombre)
        self.celdas_visitadas = set()

    def al_iniciar(self):
        pass
    

    def decidir(self, percepcion):
        vertical, horizontal = percepcion['direccion_meta']
        celda_actual = percepcion['posicion']
        self.celdas_visitadas.add(celda_actual)
        r,c = celda_actual

        if(vertical != 'ninguna' and (percepcion[vertical] == 'libre' or percepcion[vertical] == 'meta')):
            dr,dc = self.DELTAS[vertical]
            prox_celda = (r+dr, c+dc)
            if(prox_celda not in self.celdas_visitadas):
                return vertical

        if(horizontal != 'ninguna' and (percepcion[horizontal] == 'libre' or percepcion[horizontal] == 'meta')):
            dr,dc = self.DELTAS[horizontal]
            prox_celda = (r+dr, c+dc)
            if(prox_celda not in self.celdas_visitadas):
                return horizontal
            
            
        for direccion in self.ACCIONES:
            estado = percepcion[direccion]
            if(estado == 'libre' or estado == 'meta'):
                return direccion
            
        return 'abajo'