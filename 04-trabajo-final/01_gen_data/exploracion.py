import json
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import shapely.wkb as wkb
import numpy as np

from shapely.geometry import Polygon, Point



def gen_data(x0, y0, x1, y1, n_data, geometry):
    data = []
    while len(data) < n_data:
        point = Point(np.random.uniform(x0, x1), np.random.uniform(y0, y1))
        data.append(point)
    return data


def filter_points(points, polygon):
    """Filtra los puntos que están dentro y fuera del polígono."""
    points_inside = [point for point in points if point.within(polygon)]
    points_outside = [point for point in points if not point.within(polygon)]
    return points_inside, points_outside


file_path = r"C:\python\evaluacion.curso\04-trabajo-final\base.data\50001.parquet"


if __name__=="__main__":
    n_data = 10000
    df = pd.read_parquet(file_path)
    wkb_data_med = df.iloc[0,5]
    
    geometry = wkb.loads(wkb_data_med)
    gdf = gpd.GeoDataFrame(geometry=[geometry], crs='EPSG:4326')
    
    min_x, min_y, max_x, max_y = geometry.bounds
    points = gen_data(min_x, min_y, max_x, max_y, n_data, geometry)
    
    
    points_inside, points_outside = filter_points(points, geometry)
    
    x_i, y_i = zip(*[(point.x, point.y) for point in points_inside])
    x_o, y_o = zip(*[(point.x, point.y) for point in points_outside])
    
    
    
    
    
    
    
    
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax)
    
    plt.scatter(x_i, y_i, color='r', s=5)
    # plt.scatter(x_o, y_o, color='g', s=5)
    
    plt.show()
    
    