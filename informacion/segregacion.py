import pandas as pd
from datetime import datetime

fecha = datetime.now().year

# df slide 1: corporativo, comercial, compania totales para fecha
def generar_df_slide_1(data_frame_actual: pd.DataFrame, data_frame_pasado: pd.DataFrame):

    resultados_generales_actual = data_frame_actual.iloc[[9], :4]
    resultados_generales_pasado = data_frame_pasado.iloc[[9], :4]

    # invertir para que quede como la de canva
    s1 = resultados_generales_pasado.iloc[0, 1:].reset_index()
    s2 = resultados_generales_actual.iloc[0, 1:].reset_index()

    s1.columns = ["etiqueta", f"{fecha-1}"]
    s2.columns = ["etiqueta", f"{fecha}"]

    # renombrar para que quede como la de canva
    rename_map = {
        "Total": "Compañía",
        "Corporativo": "Corporativo",
        "Operativo": "Comercial"
    }

    s1["etiqueta"] = s1["etiqueta"].map(rename_map)
    s2["etiqueta"] = s2["etiqueta"].map(rename_map)

    # combinar pasado y actual para que quede como la de canva
    result1 = pd.merge(s1, s2, on="etiqueta")

    diferencias_1 = result1[f"{fecha}"] - result1[f"{fecha - 1}"]

    # print de las diferencias para que las calcule la computadora
    print("las diferencias entre periodos para la primer slide son:")
    print(diferencias_1.to_string(index=False))

    # guardar excel para actualizar canva
    result1.to_excel(f"informacion/resultados/resultados_generales_{fecha}.xlsx", index=False)

# df slide 2: corporativo, comercial, compania por area para fecha
def generar_df_slide_2(data_frame_actual: pd.DataFrame, data_frame_pasado: pd.DataFrame):

    resultados_por_dimension_actual = data_frame_actual.iloc[1:9, :4]
    resultados_por_dimension_pasado = data_frame_pasado.iloc[1:9, :4]

    # de pasado solo necesito total
    pasado = resultados_por_dimension_pasado[["Dimensión", "Total"]].copy()
    pasado.columns = ["Etiqueta", f"Compañía {fecha - 1}"]

    # del actual necesito todas las columnas
    actual = resultados_por_dimension_actual.copy()
    actual.columns = ["Etiqueta", "Compañía", "Corporativo", "Comercial"]

    # combinar pasado y actual para que quede como la de canva
    result2 = pd.merge(pasado, actual, on="Etiqueta")
    result2 = result2[["Etiqueta", f"Compañía {fecha - 1}", "Compañía", "Corporativo", "Comercial"]]

    # guardar excel para actualizar canva
    result2.to_excel(f"informacion/resultados/resultados_por_dimension_{fecha}.xlsx", index=False)

# df slide 3: comercial para la fecha vs fecha anterior, por cada area
def generar_df_slide_3(data_frame_actual: pd.DataFrame, data_frame_pasado: pd.DataFrame):
    
    resultados_comerciales_actual = data_frame_actual.iloc[1:9, [0, 3]]
    resultados_comerciales_pasado = data_frame_pasado.iloc[1:9, [0, 3]]

    # renombrar columnas para que quede como canva
    resultados_comerciales_pasado.columns = ["Etiqueta", f"Comercial {fecha - 1}"]
    resultados_comerciales_actual.columns = ["Etiqueta", f"Comercial {fecha}"]

    # combino para que quede como canva
    result_comercial = pd.merge(resultados_comerciales_pasado, resultados_comerciales_actual, on="Etiqueta")

    diferencias_2 = result_comercial[f"Comercial {fecha}"] - result_comercial[f"Comercial {fecha - 1}"]

    # print de las diferencias para que las calcule la computadora
    print("las diferencias entre periodos para la segunda slide son:")
    print(diferencias_2.to_string(index=False))

    # guardar en excel para actualizar el canva
    result_comercial.to_excel(f"informacion/resultados/resultados_comerciales_{fecha}.xlsx", index=False)

# slide 4???? que es el enp y por que no tiene sentido xd
def generar_df_slide_4():
    ...

# df slide 5: ranking de categorias por valor numerico, corporativo vs comercial
def generar_df_slide_5(data_frame_actual: pd.DataFrame, data_frame_pasado: pd.DataFrame):

    resultados_corporativos = data_frame_actual.iloc[1:9, [0, 2]]
    ranking_corporativo_actual = resultados_corporativos.sort_values(by="Corporativo", ascending=False)

    resultados_comerciales_actual = data_frame_actual.iloc[1:9, [0, 3]]
    ranking_comercial_actual = resultados_comerciales_actual.sort_values(by="Operativo", ascending=False)
    # la computadora te ordena el codigo automaticamente. solo falta ordenar manualmente las imagenes.

def segregar():

    actual = pd.read_excel(f"informacion/datos/encuesta_clima_{fecha - 1}.xlsx")
    pasado = pd.read_excel(f"informacion/datos/encuesta_clima_{fecha - 2}.xlsx")

    generar_df_slide_1(actual, pasado)
    generar_df_slide_2(actual, pasado)
    generar_df_slide_3(actual, pasado)
    # generar_df_slide_4(actual, pasado)
    generar_df_slide_5(actual, pasado)