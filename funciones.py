
import requests
import pandas as pd


def descargar_api_barna(resource_id, nombre_archivo):
    url = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search"
    
    limite = 1000
    offset = 0
    registros = []

    while True:
        params = {
            "resource_id": resource_id,
            "limit": limite,
            "offset": offset
        }

        respuesta = requests.get(url, params=params)
        datos = respuesta.json()
        filas = datos["result"]["records"]

        if not filas:
            break

        registros.extend(filas)
        offset += limite

    df = pd.DataFrame(registros)
    df.to_csv(nombre_archivo, index=False)
    return df



def informe(x):
    print("Información del DataFrame:")
    print(x.info())
    print("Descripción estadística:")
    print(x.describe())
    print("Valores nulos:")
    print(x.isnull().sum())
    print("Tipos de datos:")
    print(x.dtypes)
    print("Primeras 5 filas:")
    print(x.head())
    print("Últimas 5 filas:")
    print(x.tail())
    print("Forma del DataFrame:")
    print(x.shape)
    print("columnas")
    print(x.columns)


def analisis(x):
    print(x.value_counts())
    print(x.unique())
    print(x.nunique())


def datos(x):
    print("datos nulos")
    print(x.isnull().sum())
    print("datos totales")
    print(x.count())   
    print("porcentaje de nulos")
    print(x.isnull().sum() / x.shape[0]*100)
    print("datos duplicados")
    print(x.duplicated().sum())



def limpieza(df, column):
    df[column] = df[column].str.strip().str.upper()
    return df


def eliminar_filas_y_columnas_vacias(df):
    return (
        df
        .dropna(axis=0, how="all")
        .dropna(axis=1, how="all")
    )