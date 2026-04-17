"""
mi_agente.py — Aquí defines tu agente.
╔══════════════════════════════════════════════╗
║  ✏️  EDITA ESTE ARCHIVO                      ║
╚══════════════════════════════════════════════╝

Tu agente debe:
    1. Heredar de la clase Agente
    2. Implementar el método decidir(percepcion)
    3. Retornar: 'arriba', 'abajo', 'izquierda' o 'derecha'

Lo que recibes en 'percepcion':
───────────────────────────────
percepcion = {
    'posicion':       (3, 5),          # Tu fila y columna actual
    'arriba':         'libre',         # Qué hay arriba
    'abajo':          'pared',         # Qué hay abajo
    'izquierda':      'libre',         # Qué hay a la izquierda
    'derecha':        None,            # None = fuera del mapa

    # OPCIONAL — brújula hacia la meta.
    # No es percepción real del entorno, es información global.
    # Usarla hace el ejercicio más fácil. No usarla es más realista.
    'direccion_meta': ('abajo', 'derecha'),
}

Valores posibles de cada dirección:
    'libre'  → puedes moverte ahí
    'pared'  → bloqueado
    'meta'   → ¡la meta! ve hacia allá
    None     → borde del mapa, no puedes ir

Si tu agente retorna un movimiento inválido (hacia pared o
fuera del mapa), simplemente se queda en su lugar.
"""

from entorno import Agente
import random


class MiAgente(Agente):
    """
    Tu agente de navegación.

    Implementa el método decidir() para que el agente
    llegue del punto A al punto B en el grid.
    """

    def __init__(self):
        super().__init__(nombre="Mi Agente")
        # Puedes agregar atributos aquí si los necesitas.
        # Ejemplo:
        self.pasos = 0
        self.memoria = {"":""}


    def al_iniciar(self):
        """Se llama una vez al iniciar la simulación. Opcional."""
        pass

    def decidir(self, percepcion):
        
        """
        Decide la siguiente acción del agente.
        
        Parámetros:
            percepcion – diccionario con lo que el agente puede ver

        Retorna:
            'arriba', 'abajo', 'izquierda' o 'derecha'
        """
        vertical,horizontal = percepcion["direccion_meta"]

        if(self.memoria[pasos]):
            if(vertical != "ninguna"):
                celda = percepcion[vertical]
                if celda == "libre" or celda == "meta":
                    self.memoria[vertical] = celda
                    pasos+=1
                    return vertical
            

        if(horizontal != "ninguna"):
            celda = percepcion[horizontal]
            if celda == "libre" or celda == "meta":
                pasos+=1
                return horizontal
            

        random.shuffle(self.ACCIONES)    
        for i in self.ACCIONES:
            celda = percepcion[i]
            if celda == "libre" or celda == "meta":
                return i
                


