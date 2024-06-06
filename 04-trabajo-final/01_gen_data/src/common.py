from datetime import datetime, timedelta
import pandas as pd
import numpy as np

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
