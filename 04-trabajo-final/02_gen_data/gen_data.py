"""
Este script genera los datos de ventas, estas ventas pueden ser aleatorias
en cualquiera de las comunas, de las tiendas pero el cliente que genera la venta
ya esta especificado.

El empleado es constante durante el día pero cambia aleatoriamente entre días.
La venta es aleatoria durante el día y obedece a una distribución normal centrada
en el medio día.
"""

import pandas as pd



file_res_path = r"../base.data/datos_por_comuna2.parquet"


if __name__ == "__main__":
    cols_base = ['OBJECTID', 'CODIGO', 'NOMBRE', 'IDENTIFICACION', 'LIMITEMUNICIPIOID',
                   'SUBTIPO_COMUNACORREGIMIENTO',
                   'customer_customer_id', 'customer_name', 'customer_phone',
                   'customer_email', 'customer_address', 'employee_employee_id',
                   'employee_name', 'employee_phone', 'employee_email', 'employee_address',
                   'employee_comission'
                   ]
    df_base = pd.read_parquet(file_res_path, columns=cols_base)
    # df = df_base[cols_base]


