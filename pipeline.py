"""
Archivo principal. Maneja el flujo de la aplicacion. Llama a funciones de 1informacion/segregacion.py para generar dfs

Guarda en memoria resultados anteriores y ejecuta el flujo de 2actualizacion/generar_graficas.py

RPA con playwright actualiza las tablas con los .xlsx generados en pasos previos.
"""

from informacion.segregacion import segregar

print("corri")
segregar()

