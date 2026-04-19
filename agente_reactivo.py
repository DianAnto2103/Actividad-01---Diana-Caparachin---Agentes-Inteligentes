from entorno import Agente
from entorno import random


class AgenteReactivo(Agente): 

    #Problema: Ingresa en un bucle al encontrar libre la casilla o celda anterior
    #Posible solución: aletoriedad
    #Mejor solución: Utilizar Agente Basado en Modelos (con memoria de casillas o celdas anteriores)

    def __init__(self, nombre="Agente Reactivo Simple"):
        super().__init__(nombre)

    def al_iniciar(self):
        pass

    def decidir(self, percepcion):
        estado = percepcion[direccion]
        for direccion in self.ACCIONES:
            if(estado == 'libre' or estado == 'meta'):
                return direccion
            else:
                random.shuffle(self.ACCIONES)
        return 'abajo'
