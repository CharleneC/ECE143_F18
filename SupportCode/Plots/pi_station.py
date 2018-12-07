#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Jiaqi Yan, Arun Joseph
"""

# how to use create_pi_station_distribution(year=2017,day='Weekday') 

import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Pie
from PIL import Image
import glob
#from pyecharts import WorldCloud

def station_entrance(station,filename,*,day='Weekday'):
    """
    Function returns the stations exit

    Args:
        station (str) : name of the station 2letter code
        filename (str) : path to the file

    Kwargs:
        day (str) : sheet to read (valid options 'Weekday,Saturday,Sunday')

    Returns:
        number of entries from the station
    """
    assert isinstance(station,str) and len(station) == 2
    assert isinstance(filename,str)
    assert day in ['Weekday','Saturday','Sunday']

    sheet_name_lookup = dict(zip(['Weekday','Saturday','Sunday'],[0,1,2]))
    sheet_name = sheet_name_lookup[day]
    #read data
    data = pd.read_excel(filename,sheet_name)
    station_list = list(data.iloc[: , 0])
    try:
        loc = station_list.index(station)
    except ValueError:
        return 0
    Entry_loc = station_list.index('Entries')
    exist_list = data.iloc[loc]
    sta_exist = exist_list[Entry_loc]
    return int(sta_exist)



def create_pi_station_distribution(year,*,Data_path = 'Data/',Save_loc='Outputs/',verbose=True,day='Weekday'):
    '''
    Creates a pie chart for the station traffic for the year specified

    Args:
        year (int) : year for which pie chart is to be created

    Kwargs:
        Data_loc (str) : location of BART data [default = 'Data/']
        Save_loc (str) : folder to which images are to be saved [Default = 'Outputs/']
        verbose (bool) : set to True for viewing the progress
        day (str) : feeds into station_entrance check function to see description
    '''
    assert isinstance(year,int)
    assert year >= 2001 and year <=2018 , 'Data available only for range (2001,2018)'
    assert isinstance(Data_path,str), "please provide a valid folder path"
    assert isinstance(Save_loc,str) , "please provide a valide folder path"

    fo = pd.read_excel('Data/Station_Names.xls')
    station_name_list = fo.iloc[: , 0:2].values
    station_name_lookup=dict(zip(station_name_list[:,1],station_name_list[:,0]))
    
    file_list = glob.glob(Data_path+'ridership_'+str(year)+'/*.xls*')
    assert len(file_list)>0, f"No xls or xlsx files found in the location {Data_loc}/ridership_{str(year)}"

    # find the overall ridership for the year
    rider_dict = {}
    for i,file_ in enumerate(file_list):
        if verbose:
            print(f'Processing file {i+1}/{len(file_list)}')
        for name in station_name_list:
            station = str(name[1])
            rides = station_entrance(station,file_,day=day)
            if rides:
                try:
                    rider_dict[station]+=rides
                except:
                    rider_dict[station] = rides

    rider_list = sorted(rider_dict.items(), key=lambda d: d[1], reverse=True)
    last10_list = rider_list[-12:]
    top_dict = dict(rider_list[:-12])
    last10_sum = 0
    for tup in last10_list:
        last10_sum += tup[1]
    top_dict['others'] = last10_sum
    station_name_lookup['others'] = 'Bottom 12 Stations'
    attr,v = zip(*top_dict.items())
    attr_full = list(map(lambda x:station_name_lookup[x],attr))
    
    
    pie =Pie(f'{day} station traffic for {year}')
    pie.add('', attr_full, v, radius=[40,60], is_label_show=True,is_legend_show=False)

    try:
        pie.render(path=Save_loc+'station_traffic_'+day+'_'+str(year)+'.png')
    except:
        import os
        os.makedirs(Save_loc, exist_ok=True)
        pie.render(path=Save_loc+'station_traffic_'+day+'_'+str(year)+'.png')


