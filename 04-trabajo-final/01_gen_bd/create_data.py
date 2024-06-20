# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:52:28 2024

@author: mfceb
"""


import pandas as pd
import numpy as np

from datetime import datetime, timedelta
from src import leer_archivo_comuna, distribuir_personas_comunas, asociar_comunas
from src import calcular_data, asociar_com_empl, gen_id_user_comuna
from src import generar_order_id, obtener_coordenadas, gen_datetime
import os


file_path = "01_gen_bd/data/1. Proyecciones Medellín por Comunas y Corregimientos 2018 - 2030.xlsx"

file_comunas_path = r"base.data/medellin_neighborhoods.parquet"
file_res_path = r"base.data/"
file_customers = r'base.data/customers.parquet'
file_employees = r'base.data/employees.parquet'




if __name__ == "__main__":
    fecha = "03/04/2024"
    time = datetime.now().strftime('%S:%M:%H').replace(':','')
    name_file = f"{time}{fecha.replace('/','')}.parquet"
    n_dias = 2    
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    # datetime.strptime(f.strftime("%Y/%m/%d"), "%Y/%m/%d") 
    f_temp = [fecha + timedelta(days=d) for d in range(n_dias)]    
    fechas = [datetime.strptime(f.strftime("%Y/%m/%d"), "%Y/%m/%d") for f in f_temp]   
    df_parquet = pd.DataFrame()
    
    n_datos = 1000
    
    df_com = leer_archivo_comuna(file_path)
    df_cust = pd.read_parquet(file_customers)
    df_empl = pd.read_parquet(file_employees)
    
    df_cust = distribuir_personas_comunas(df_cust, df_com)    
    df_empl = distribuir_personas_comunas(df_empl, df_com)    
    df_comunas = pd.read_parquet(file_comunas_path) 
    df_comunas = df_comunas.dropna(subset=['NOMBRE']) 
    
    df_com = calcular_data(df_com, n_datos)
    df_com = asociar_comunas(df_comunas, df_com)
    
    df_com = asociar_com_empl(df_com, df_empl, 'empl')

    df_cust = gen_id_user_comuna(df=df_cust, df_com=df_com)    
    l_fecha = gen_datetime(fecha, df_cust.shape[0])    
    df_cust['fecha'] = l_fecha
    df_cust = df_cust.sort_values(by='fecha', ascending=False)
    
    
#     df_cust[['latitude', 'longitude']] = df_cust['points'].apply(lambda geom: pd.Series(obtener_coordenadas(geom)))    
#     df_cust['event_date'] = df_cust['fecha'].astype(str)
#     df_cust[['event_date', 'event_hour']] = df_cust['event_date'].str.split(' ', expand=True)
#     df_cust[['event_year', 'event_month', 'event_day']] = df_cust['event_date'].str.split('-', expand=True)
#     df_cust[['event_hour', 'event_minute', 'event_second']] = df_cust['event_hour'].str.split(':', expand=True)
    
#     df_cust['partition_date'] = df_cust['event_day'] +  df_cust['event_month'] + df_cust['event_year']

#     df_cust = df_cust.rename(columns={'NOMBRE': 'neighborhood'})
#     df_cust = df_cust.rename(columns={'IDENTIFICACION': 'commune'})
#     df_cust = df_cust.rename(columns={'empl_employee_id': 'employee_id'})    
    array = list(map(int, np.random.uniform(1, 30, df_cust.shape[0])))
    df_cust['quantity_products'] = array    
#     generar_order_id(df_cust)
    
    
#     cols =['partition_date', 'order_id', 'commune', 'customer_id', 'employee_id', 
#             'event_date', 'event_day', 'event_hour', 'event_minute', 
#             'event_month', 'event_second', 'event_year', 'latitude', 'longitude',
#             'neighborhood', 'quantity_products']
#     df_cust = df_cust[cols]    
    
    file_parquet = f"{file_res_path}{name_file}" #datos crudos pesados
    df_cust.to_parquet(os.path.join("warehouse/raw", name_file))
    
    
    
    
    
    
    
    
    
    
    
    
    