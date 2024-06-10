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


from src import leer_archivo_comuna, calcular_data, gen_datetime, asociar_comunas, gen_data, generar_coordenadas

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



if __name__ == "__main__":
    # np.random.seed(43)
    fecha = "03/04/2024"
    n_dias = 2
    
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    f_temp = [fecha + timedelta(days=d) for d in range(n_dias)]
    
    fechas = [datetime.strptime(f.strftime("%Y/%m/%d"), "%Y/%m/%d") for f in f_temp]    

    df_parquet = pd.DataFrame()
    
    for cont, fecha in enumerate(fechas):
        print('*'.center(50, '*'))
        print(cont)
        print('*'.center(50, '*'))
        n_datos = 1000
        
        df_i = leer_archivo_comuna(file_path)
        df_cust = pd.read_parquet(file_customers)
        df_empl = pd.read_parquet(file_employees)
        df_comunas = pd.read_parquet(file_comunas_path) 
        

        df_com_base = calcular_data(df_i, n_datos)
    
        # df_comunas = pd.read_parquet(file_comunas_path)    
        df = asociar_comunas(df_comunas, df_com_base)
        
        df = generar_coordenadas(df)
        l_fecha = gen_datetime(fecha, df.shape[0])
        df['FECHA'] = l_fecha    
        
        # df_cust = pd.read_parquet(file_customers)
        df = asociar_id_elm1_elm2(df_cust, df, 'customer')
        
        # df_empl = pd.read_parquet(file_employees)
        df = asociar_id_elm1_elm2(df_empl, df, 'employee')  
        
        df_parquet = pd.concat([df_parquet, df], ignore_index=True)
    
    df_parquet.to_parquet(file_res_path)

    
