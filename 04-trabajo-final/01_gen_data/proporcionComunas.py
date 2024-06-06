# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:52:28 2024

@author: mfceb
"""

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


import shapely.wkb
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkb
from shapely.geometry import Point

from src import leer_archivo_comuna, calcular_data, gen_datetime, asociar_comunas

file_path = r"data\1. Proyecciones Medellín por Comunas y Corregimientos 2018 - 2030.xlsx"

file_comunas_path = r"../base.data/medellin_neighborhoods.parquet"
file_res_path = r"../base.data/datos_por_comuna.parquet"

import numpy as np
from shapely.geometry import Point

def gen_data(data):
    geometry = shapely.wkb.loads(data['geometry'])[0]
    x0, y0, x1, y1 = geometry.bounds
    n_data = list(data.Ponerado)[0]
    points = []
    while len(points) < n_data:
        point = Point(np.random.uniform(x0, x1), np.random.uniform(y0, y1))
        if point.within(geometry):
            # points.append(point)
            points.append(wkb.dumps(point))
    n = len(points)
    base = data.iloc[0]
    n_base = pd.concat([base]*(n-1), axis=1).transpose()
    df = pd.concat([data, n_base], ignore_index=True)
    df['points'] = points
    df['geometry'] = list(data['geometry'])[0]
    return df


def generar_coordenadas(df):
    df_res = pd.DataFrame()
    comunas = list(df.NOMBRE)
    df['puntos'] = ''
    df['FECHA'] = ''
    for comuna in comunas:
        if comuna==None:
            continue
        msk = df.NOMBRE==comuna
        d_comuna = df.loc[msk]
        df_comuna = gen_data(d_comuna)
        df_res = pd.concat([df_res, df_comuna], ignore_index=True)
    
    cols = ['OBJECTID', 'CODIGO', 'NOMBRE', 'IDENTIFICACION', 'LIMITEMUNICIPIOID',
            'SUBTIPO_COMUNACORREGIMIENTO', 'LINK_DOCUMENTO', 'SHAPEAREA', 'FECHA',
            'SHAPELEN', 'Ponerado', 'puntos', 'points', 'geometry']
    df_res = df_res[cols]
    return df_res

if __name__ == "__main__":
    # np.random.seed(43)
    fecha = "03/06/2024"
    fecha = datetime.strptime(fecha, "%d/%m/%Y")  
    
    df_i = leer_archivo_comuna(file_path)
    
    # porcentaje, definimos un 5%
    n_datos = 1000
    df_com_base = calcular_data(df_i, n_datos)

    df_comunas = pd.read_parquet(file_comunas_path)    
    df = asociar_comunas(df_comunas, df_com_base)
    
    # cargamos la geometria
    df = generar_coordenadas(df)
    l_fecha = gen_datetime(fecha, df.shape[0])
    df['FECHA'] = l_fecha
    
    
    df.to_parquet(file_res_path)


