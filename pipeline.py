"""
Archivo principal. Maneja el flujo de la aplicacion. Llama a funciones de 1informacion/segregacion.py para generar dfs

Guarda en memoria resultados anteriores y ejecuta el flujo de 2actualizacion/generar_graficas.py

RPA con playwright actualiza las tablas con los .xlsx generados en pasos previos.
"""
import pandas as pd
from datetime import datetime

fecha = datetime.now().year

from informacion.segregacion import generar_df_slide_1, generar_df_slide_2, generar_df_slide_3, generar_df_slide_4, generar_df_slide_5, generar_df_slide_6
from actualizacion.actualizar_graficas import usar_canva

actual = pd.read_excel(f"informacion/datos/encuesta_clima_{fecha - 1}.xlsx")
pasado = pd.read_excel(f"informacion/datos/encuesta_clima_{fecha - 2}.xlsx")

diferencias_1, path_1 = generar_df_slide_1(actual, pasado)
path_2 = generar_df_slide_2(actual, pasado)
diferencias_2, path_3 = generar_df_slide_3(actual, pasado)
# generar_df_slide_4(actual, pasado)
generar_df_slide_5(actual)
generar_df_slide_6(actual, pasado)

usar_canva([path_1, path_2, path_3], [diferencias_1, diferencias_2])