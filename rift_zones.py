import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import pandas as pd
import numpy as np
import os
from pathlib import Path
from shapely.geometry import Point

from zone_names import rift_zones
from zone_polygons import rift_zone_polygons

def calc_dist_vect(x1, x2, y1, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dist_from_mid_line(x=None, y=None):
    dy = 15000
    dx = -15000
    y1 = 0
    x1 = 15000
    det = 450000000

    a = (dy*(y-y1)+dx*(x-x1))/det
    closest_x = x1+a*dx
    closest_y = y1+a*dy

    if type(x) == pd.Series:
        df = pd.DataFrame({
            'x': x,
            'y': y,
            'mid_x': closest_x,
            'mid_y': closest_y,
            'dist': calc_dist_vect(x, closest_x, y, closest_y)
        })

        df['dist'] = calc_dist_vect(x, closest_x, y, closest_y)
        df.loc[calc_dist_vect(x, 0, y, 0) < calc_dist_vect(x, 15000, y, 15000), 'dist'] *= -1

        return df['dist']

    dist = calc_dist_vect(x, closest_x, y, closest_y)
    if calc_dist_vect(x, 0, y, 0) < calc_dist_vect(x, 15000, y, 15000):
        dist *= -1

    return dist

def get_polygon(zone=None):
    rift_zone_dict = {'zone': rift_zones, 'geometry': rift_zone_polygons}
    rift_polygon_df = gpd.GeoDataFrame(rift_zone_dict)
    return rift_polygon_df[rift_polygon_df['zone']==zone].reset_index()['geometry'][0]

def plot_polygon(zone=None):
    polygon1 = get_polygon(zone)
    x,y = polygon1.exterior.xy
    plt.plot(x,y)

def find_nearest_zone(pos_x, pos_y, zone_polygons, zone_names):
    """
    Find the nearest zone to a given position (x, y) if the position is not inside any zone.
    """
    
    player_point = Point(pos_x, pos_y)
    min_distance = float('inf')
    nearest_zone = None

    for zone_name, polygon in zip(zone_names, zone_polygons):
        # Calculate the distance from the point to the polygon's centroid
        distance = player_point.distance(polygon.centroid)
        if distance < min_distance:
            min_distance = distance
            nearest_zone = zone_name

    return nearest_zone

def assign_zone_names(df):
    df['zone_name'] = df.apply(lambda row: find_nearest_zone(row['pos_x'], row['pos_y'], rift_zone_polygons, rift_zones), axis=1)
    return df

def show_zone(zone=None, pos_df=None, plot_x=None, plot_y=None, shift=50, fig_size=(15,15)):

    plt.figure(figsize=fig_size)
    map_img = mpimg.imread(os.path.join(os.path.dirname(Path.cwd()), 'rift-zones\\resources\\Map.png'))
    plt.imshow(map_img, extent=(0,15000,0,15000))
    plt.axis('off')
    if zone is not None:
        if type(zone) is list:
            for z in zone:
                try:
                    plot_polygon(z)
                except:
                    print(f'Could not find {z}')
        else:
            plot_polygon(zone)
    else:
        for zone in rift_zones:
            plot_polygon(zone)

    if pos_df is not None:
        if 'distance_from_player' in pos_df.columns:
            for i in range(len(pos_df)):
                if pos_df.reset_index()['distance_from_player'][i] <= 2000:
                    fmt = 'co'
                else:
                    fmt = 'wo'
                plt.plot(pos_df.reset_index()['pos_x'][i]+shift, pos_df.reset_index()['pos_y'][i]+shift, fmt)
        else:
            points = list(zip(pos_df.pos_x, pos_df.pos_y))
            for x,y in points:
                plt.plot(x+shift, y+shift, 'wo')

    if pos_df is None and plot_x is not None and plot_y is not None:
        plt.plot(plot_x, plot_y, 'wo')

    plt.show()


