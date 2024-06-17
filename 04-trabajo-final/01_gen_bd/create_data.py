# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:52:28 2024

@author: mfceb
"""

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from shapely.geometry import Point
import shapely.wkb
import geopandas as gpd
from shapely import wkb



# from src import leer_archivo_comuna, calcular_data, gen_datetime, asociar_comunas, gen_data, generar_coordenadas

file_path = r"data\1. Proyecciones Medellín por Comunas y Corregimientos 2018 - 2030.xlsx"

file_comunas_path = r"../base.data/medellin_neighborhoods.parquet"
file_res_path = r"../base.data/datos_por_comuna2.parquet"
file_customers = r'../base.data/customers.parquet'
file_employees = r'../base.data/employees.parquet'


def asociar_id_elm1_elm2(df, df_comuna, tipo):
    """
    asocia dos dataframes, elemento1 y elemento 2.
    Pueden ser usuarios y comunas, se crea las columnas para la union.
    Pueden ser empleados y comunas, se crea las columnas para la union.
    """
    new_col = 'ID_aux'
    # renombrar las columnas segun el tipo
    cols = {col:f"{tipo}_{col}" for col in df.columns}
    df.rename(columns=cols, inplace=True)
    n_data = df_comuna.shape[0]
    array = np.random.uniform(0, df.shape[0], n_data)
    array = list(map(int, array))
    n_cust = [i for i in range(df.shape[0])]
    df[new_col] = n_cust
    df_comuna[new_col] = array
    df_res = pd.merge(df_comuna, df, on=new_col, how='inner')
    df_res.drop(new_col, axis=1, inplace=True)
    return df_res



def leer_archivo_comuna(path, anno = 2024):    
    df = pd.read_excel(path, skiprows=15, nrows=23)
    df.drop(0, inplace=True)
    df[['num', 'Comuna']] = df[df.columns[0]].str.split(pat=' ', n=1, expand=True)
    df.reset_index(drop=True, inplace=True)
    cols = ['Comuna', anno]
    df = df[cols]
    total = df[anno][21]
    df['Proporcion'] = df[[anno]]/total
    df['Comuna'] = df['Comuna'].str.upper()
    df['Comuna'] = df['Comuna'].apply(lambda x: x.replace(' - ', ' ') if pd.notna(x) else x)
    mask = df.Comuna == 'BELEN'
    df.loc[mask, 'Comuna'] = 'BELÉN'
    df = df.iloc[:-1]
    df['id_comuna'] = [i for i in range(1, df.shape[0] + 1)]
    return df

def calcular_data(df, size=1000):
    pesos = df.Proporcion.tolist()
    df['Ponderados'] = [int(np.random.uniform(prop*3/4, prop+prop/2)*size) for prop in pesos]
    return df


def asociar_comunas(df1, df2):   
    cols_d1 = list(df1.NOMBRE)
    cols_d2 = list(df2.Comuna)    
    for c1 in cols_d1:
        for c2 in cols_d2:
            if c2 in c1:
                val = list(df2[df2.Comuna==c2].Ponderados)[0]
                id_com = list(df2[df2.Comuna==c2].id_comuna)[0]
                msk = df1.NOMBRE==c1                
                df1.loc[msk, 'Ponerado'] = val
                df1.loc[msk, 'id_comuna'] = id_com
    return df1


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
        # if df_res.shape[0] > 0:
        df_res = pd.concat([df_res, df_comuna], ignore_index=True)    
    cols = ['OBJECTID', 'CODIGO', 'NOMBRE', 'IDENTIFICACION', 'LIMITEMUNICIPIOID',
            'SUBTIPO_COMUNACORREGIMIENTO', 'LINK_DOCUMENTO', 'SHAPEAREA', 'FECHA',
            'SHAPELEN', 'Ponerado', 'puntos', 'points', 'geometry']
    df_res = df_res[cols]
    return df_res


def gen_id_user_comuna(df, n_data):
    # df['id_user']  = np.random.uniform(1, n_data, df.shape[0])
    df['id_user']  = np.random.randint(1, n_data, size=df.shape[0])
    return df
    


if __name__ == "__main__":
    fecha = "03/04/2024"
    n_dias = 2    
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    f_temp = [fecha + timedelta(days=d) for d in range(n_dias)]    
    fechas = [datetime.strptime(f.strftime("%Y/%m/%d"), "%Y/%m/%d") for f in f_temp]   
    df_parquet = pd.DataFrame()
    
    n_datos = 10000
    
    df_i = leer_archivo_comuna(file_path)
    df_cust = pd.read_parquet(file_customers)
    df_empl = pd.read_parquet(file_employees)
    df_comunas = pd.read_parquet(file_comunas_path)  
    df_comunas = df_comunas.dropna(subset=['NOMBRE'])
    df_com_base = calcular_data(df_i, n_datos)    
    df = asociar_comunas(df_comunas, df_com_base)
    
    # df_cust = gen_id_user_comuna(df=df_cust, n_data=df.shape[0])
    
    
    
    # df = generar_coordenadas(df)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    