
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

from shapely.geometry import Point
import shapely.wkb
import geopandas as gpd
from shapely import wkb
import uuid






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
    df['Porcentaje'] = df[[anno]]/total*100
    df['Porcentaje'] = df['Porcentaje'].apply(math.ceil)
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
                df1.loc[msk, 'Ponderado'] = val
                df1.loc[msk, 'id_comuna'] = id_com
                df1.loc[msk, 'comuna2'] = c2
    df1.reset_index(inplace=True, drop=True)
    return df1


def gen_data(data):
    geometry = shapely.wkb.loads(data['geometry'])[0]
    x0, y0, x1, y1 = geometry.bounds
    n_data = list(data.Ponderado)[0]
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

    
def gen_id_user_comuna(df, df_com):
    n_por_comuna = df['comuna'].value_counts().sort_index().to_dict()
    df_com['id_user'] = 0
    df_arrays = df_com[['comuna2', 'Ponderado']]
    df_tmp = pd.DataFrame()
    for k, rng in n_por_comuna.items():
        msk = df_arrays.comuna2==k
        n = int(list(df_arrays[df_arrays.comuna2==k]['Ponderado'])[0])
        array = [int(np.random.uniform(0, rng)) for i in range(n)]
        tmp = df_com[msk]
        coord = gen_data(tmp)
        tmp = pd.concat([tmp] * n, ignore_index=True)
        
        tmp['geometry'] = coord['geometry']    
        tmp['points'] = coord['points']    
        tmp['id_count_comuna'] = array
        
        tmp2 = df[df.comuna==k]
        #hacer el join de tmp y tmp2
        tmp = pd.merge(tmp, tmp2, on='id_count_comuna', how='left')   
        
        df_tmp = pd.concat([df_tmp, tmp], ignore_index=True)
        
        
        
        
    return df_tmp


def distribuir_personas_comunas(df_p, df_c):
    n_p = df_p.shape[0]
    n_c = df_c.shape[0]
    if n_p >= n_c:
        df_c['Proporcion'] = df_c['Proporcion'].astype(float)
        comunas = np.random.choice(df_c['Comuna'], size=n_p, p=df_c['Proporcion'])    
        df_p['comuna'] = comunas
        df_p = df_p.sort_values(by='comuna')
        df_p.reset_index(drop=True, inplace=True)
        n_por_comuna = df_p['comuna'].value_counts().sort_index()
        df_p['id_count_comuna']  = [j for i in n_por_comuna for j in range(i)]
        df_p = df_p.sort_values(by=['comuna', 'id_count_comuna'])
        df_p.reset_index(drop=True, inplace=True)
        return df_p
    else:
        df = pd.DataFrame()
        personas_por_comuna = np.ceil(df_c['Proporcion'] * n_p).astype(int)
        personas_rep = np.tile(df_p['name'], personas_por_comuna.sum())[:n_c]
        np.random.shuffle(personas_rep)
        for p in personas_rep:
            df2 = df_p[df_p.name==p]
            df = pd.concat([df, df2], ignore_index=True)
        df_p = df
        df_p['comuna'] = df_c['Comuna']
        return df_p

def conv_seg(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seconds = segundos % 60
    return timedelta(hours=horas, minutes=minutos, seconds=int(seconds))


def set_fecha(fech):
    fech = fech
    def sumaFecha(i):
        return fech + i
    return sumaFecha


def gen_datetime(fecha, cantidad):
    n = 86400
    l_seg = np.random.normal(loc=n/2, scale=n/6, size=cantidad)
    l_seg = np.clip(l_seg, 0, n)
    res = map(conv_seg, l_seg)    
    f = set_fecha(fecha)
    res = map(f, res)    
    return list(res)

def obtener_coordenadas(punto):
    geo = wkb.loads(punto)
    return geo.x, geo.y


def asociar_com_empl(df_com, df_empl, tipo):
    cols = {col:f"{tipo}_{col}" for col in df_empl.columns}
    df_empl.rename(columns=cols, inplace=True)
    df_empl = df_empl.rename(columns={f'{tipo}_comuna': 'comuna2'})
    # df_com = df_com.rename(columns={'comuna2': 'comuna'})
    df_res = pd.merge(df_com, df_empl, on='comuna2', how='left')   
    return df_res

def generar_order_id(df):
    def gen_order_id(elm):
        namespace = uuid.uuid4()
        return str(uuid.uuid5(namespace, elm))
    cols =['event_date', 'event_hour','event_minute','event_second', 
           'customer_id','employee_id','quantity_products'] 
    df_base = df[cols]
    df_base = df_base.astype(str)
    lista = list(map(gen_order_id, df_base.apply(lambda row: '-'.join(row.values), axis=1)))    
    df['order_id'] = lista
    return df

