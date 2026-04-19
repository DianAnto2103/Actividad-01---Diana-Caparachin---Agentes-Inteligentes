"""
main.py — Ejecuta tu agente en el Grid World.

Uso:
    python main.py

Configuración:
    Modifica las variables de abajo para cambiar el mapa.
"""

from entorno import GridWorld
from agente_utilidad import MiAgente
from agente_reactivo import AgenteReactivo
from agente_modelos import AgenteBModelo
from agente_objetivos import AgenteBObjetivos

# ── Configuración del mapa ───────────────────────
FILAS     = 10      # Alto del mapa
COLUMNAS  = 10       # Ancho del mapa
SEMILLA   = 40       # Cambiar para generar otro mapa
PAREDES   = 0.40    # Porcentaje de paredes (0.0 a 0.40)
VELOCIDAD = 0.15     # Segundos entre pasos (menor = más rápido)
MAX_PASOS = 50      # Máximo de pasos antes de rendirse
# ─────────────────────────────────────────────────

# Crear el mundo
mundo = GridWorld(
    filas=FILAS,
    columnas=COLUMNAS,
    semilla=SEMILLA,
    porcentaje_paredes=PAREDES,
)

# Mostrar mapa en consola
mundo.mostrar_mapa()

# Crear tu agente
agente = AgenteBObjetivos()

# Ejecutar con animación
resultado = mundo.animar(agente, max_pasos=MAX_PASOS, velocidad=VELOCIDAD)