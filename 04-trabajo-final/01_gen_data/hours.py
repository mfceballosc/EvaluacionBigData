import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


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
    return res


# Ejemplo de uso
fecha = "03/06/2024"
fecha = datetime.strptime(fecha, "%d/%m/%Y")

cantidad_datos = 150000
l_fecha = gen_datetime(fecha, cantidad_datos)

# Convertir las horas a horas del día (float) para el trazado
horas_del_dia = [(hora.hour + hora.minute / 60 + hora.second / 3600) for hora in l_fecha]

# # Trazar la distribución
# plt.figure(figsize=(10, 6))
# plt.hist(horas_del_dia, bins=1000, density=True, alpha=0.7, color='blue')
# plt.title('Distribución de Horas alrededor del Mediodía')
# plt.xlabel('Hora del Día')
# plt.ylabel('Densidad de Probabilidad')
# plt.grid(True)
# plt.show()
