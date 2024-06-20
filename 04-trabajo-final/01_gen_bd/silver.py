"""
Generar Silver
"""

from src import generar_order_id
import pandas as pd
import os

def load_parquet():
        dire = "base.data"
        base = "16232203042024.parquet"
        df_cust = pd.read_parquet(os.path.join(dire, "\\",base))

def silver(df_cust):
        df_cust[['latitude', 'longitude']] = df_cust['points'].apply(lambda geom: pd.Series(obtener_coordenadas(geom)))    
        df_cust['event_date'] = df_cust['fecha'].astype(str)
        df_cust[['event_date', 'event_hour']] = df_cust['event_date'].str.split(' ', expand=True)
        df_cust[['event_year', 'event_month', 'event_day']] = df_cust['event_date'].str.split('-', expand=True)
        df_cust[['event_hour', 'event_minute', 'event_second']] = df_cust['event_hour'].str.split(':', expand=True)
        df_cust['partition_date'] = df_cust['event_day'] +  df_cust['event_month'] + df_cust['event_year']
        df_cust = df_cust.rename(columns={'NOMBRE': 'neighborhood'})
        df_cust = df_cust.rename(columns={'IDENTIFICACION': 'commune'})
        df_cust = df_cust.rename(columns={'empl_employee_id': 'employee_id'})    
        generar_order_id(df_cust)

        cols =['partition_date', 'order_id', 'commune', 'customer_id', 'employee_id', 
                'event_date', 'event_day', 'event_hour', 'event_minute', 
                'event_month', 'event_second', 'event_year', 'latitude', 'longitude',
                'neighborhood', 'quantity_products']
        df_cust = df_cust[cols]

        file_name = df_cust["partition_date"][0]

        df_cust.to_parquet(file_name)