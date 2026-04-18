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
        self.visitados = set()
        self.ultima_posicion = None 


    def al_iniciar(self):
        """Se llama una vez al iniciar la simulación. Opcional."""
        self.pasos = 0
        self.visitados.clear()
        self.ultima_posicion = None

    def decidir(self, percepcion):  
        """
        Decide la siguiente acción del agente.
        
        Parámetros:
            percepcion – diccionario con lo que el agente puede ver

        Retorna:
            'arriba', 'abajo', 'izquierda' o 'derecha'
        """

        #Aqui lo que se hace es guardar la posición actual, en este caso: (0,0)
        pos_actual = percepcion['posicion'] #pos_actual = (0,0) [inicial]

        #ACTUALIZAMOS MEMORIA
        self.visitados.add(pos_actual) #agregar en los visitados
        self.pasos += 1 #aumentar pasos
        vertical,horizontal = percepcion["direccion_meta"] #vertical, horizontal tendrán la dirección meta -> (abajo, derecha)

        #INICIAMOS UTILIDAD
        utilidad = {'arriba': 0, 'abajo': 0, 'izquierda': 0, 'derecha': 0} #Calcular utilidad.


        for direccion in self.ACCIONES:
            estado = percepcion[direccion] #estado = libre, meta, pared, none; depende de direccion
            dr, dc = self.DELTAS[direccion] # guardamos los deltas correspondientes a direccion(arriba, abajo, iz, derecha)
            r,c = pos_actual #guardamos pos_actual en r,c. Ejmplo: (0,0)
            nueva_posicion = (dr+r, dc+c) #Calculamos la nueva posición correspondiente a la suma de pos actual con el movimiento realizado

        return 'abajo'
            
            

                


