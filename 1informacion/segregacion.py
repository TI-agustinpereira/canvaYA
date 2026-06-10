import pandas as pd
from datetime import datetime

fecha = datetime.now().year

# para el periodo anterior, solo guardo los valores de cada area general pues es el unico que se usa

def cargar_y_segregar_excel() -> list[pd.DataFrame]:

    df_para_cada_slide = []

    data_frame = pd.read_excel(f"datos/encuesta_clima_{fecha - 1}.xlsx")
    data_frame_pasado = pd.read_excel(f"datos/encuesta_clima_{fecha - 2}.xlsx")
    
    # df slide 1: corporativo, comercial, compania totales para fecha

    resultados_generales_actual = data_frame.iloc[[9], :4]
    resultados_generales_pasado = data_frame_pasado.iloc[[9], :4]

    # Transpose
    s1 = resultados_generales_pasado.iloc[0, 1:].reset_index()
    s2 = resultados_generales_actual.iloc[0, 1:].reset_index()

    s1.columns = ["etiqueta", f"{fecha-1}"]
    s2.columns = ["etiqueta", f"{fecha}"]

    # Rename
    rename_map = {
        "Total": "Compañía",
        "Corporativo": "Corporativo",
        "Operativo": "Comercial"
    }

    s1["etiqueta"] = s1["etiqueta"].map(rename_map)
    s2["etiqueta"] = s2["etiqueta"].map(rename_map)

    # Merge
    result1 = pd.merge(s1, s2, on="etiqueta")
    result1.to_excel(f"resultados/resultados_generales_{fecha}.xlsx", index=False)
    df_para_cada_slide.append(result1)

    
    # df slide 2: corporativo, comercial, compania por area para fecha

    resultados_por_dimension_actual = data_frame.iloc[1:9, :4]
    df_para_cada_slide.append(resultados_por_dimension_actual)
    resultados_por_dimension_actual.to_excel(f"resultados/resultados_por_dimension_{fecha}.csv", index=False)

    # df slide 3: comercial para la fecha vs fecha anterior, por cada area

    resultados_comerciales_actual = data_frame.iloc[1:9, [0, 3]]
    df_para_cada_slide.append(resultados_comerciales_actual)
    resultados_comerciales_actual.to_excel(f"resultados/resultados_comerciales_{fecha}.csv", index=False)

    # slide 4???? que es el enp y por que no tiene sentido xd

    # df slide 5: ranking de categorias por valor numerico, corporativo vs comercial

    resultados_corporativos = data_frame.iloc[1:9, [0, 2]]
    ranking_corporativo_actual = resultados_corporativos.sort_values(by="Corporativo", ascending=False)

    ranking_comercial_actual = resultados_comerciales_actual.sort_values(by="Operativo", ascending=False)

    # la computadora te ordena el codigo automaticamente. solo falta ordenar los valores.
    df_para_cada_slide.append(ranking_comercial_actual)
    df_para_cada_slide.append(ranking_corporativo_actual)

    # Verificá primero cómo se llaman las columnas
    print(resultados_corporativos.columns.tolist())


    return df_para_cada_slide

lista_dfs = cargar_y_segregar_excel()

for df in lista_dfs:
    print(df)
    print()
