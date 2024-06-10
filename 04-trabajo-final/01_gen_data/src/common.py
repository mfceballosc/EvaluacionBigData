from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from shapely.geometry import Point
import shapely.wkb
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkb


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
    # df['Comuna'] = df['Comuna'].apply(lambda x: x.replace(' - ', ' '))
    df['Comuna'] = df['Comuna'].apply(lambda x: x.replace(' - ', ' ') if pd.notna(x) else x)
    mask = df.Comuna == 'BELEN'
    df.loc[mask, 'Comuna'] = 'BELÉN'
    df = df.iloc[:-1]
    return df


def calcular_data(df, size=1000):
    pesos = df.Proporcion.tolist()
    df['Ponderados'] = [int(np.random.uniform(prop*3/4, prop+prop/2)*size) for prop in pesos]
    # df['Ponderados'] = [int(np.random.uniform(prop*3/4, prop+prop/2) * size) if prop == 0 else 1 for prop in pesos]
    return df


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


def asociar_comunas(df1, df2):   
    cols_d1 = list(df1.NOMBRE)
    cols_d2 = list(df2.Comuna)    
    for c1 in cols_d1:
        if c1 is None:
            continue
        for c2 in cols_d2:
            if c2 is None:
                continue
            # print(c1, c2)
            if c2 in c1:
                val = list(df2[df2.Comuna==c2].Ponderados)[0]
                msk = df1.NOMBRE==c1                
                df1.loc[msk, 'Ponerado'] = val
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


