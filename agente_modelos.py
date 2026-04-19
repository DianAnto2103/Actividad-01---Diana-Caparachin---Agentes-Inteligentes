from entorno import Agente


class AgenteBModelo(Agente):

    #Agente con memoria de casilla anterior (util para evitar bucles infinitos)

    def __init__(self, nombre="Agente Basado en Modelos"):
        super().__init__(nombre)
        self.celdas_visitadas = set()


    def al_iniciar(self):
        pass

    def decidir(self, percepcion):
        celda_actual = percepcion['posicion']
        self.celdas_visitadas.add(celda_actual)
        for direccion in self.ACCIONES:
            estado = percepcion[direccion]
            if(estado == 'libre' or estado == 'meta'):
                dr,dc = self.DELTAS[direccion]
                r,c = celda_actual
                prox_celda = (r+dr, c+dc)
                if(prox_celda not in self.celdas_visitadas):
                    return direccion
        
        for direccion in self.ACCIONES:
            estado = percepcion[direccion]
            if(estado == 'libre' or estado == 'meta'):
                return direccion
        return 'abajo'