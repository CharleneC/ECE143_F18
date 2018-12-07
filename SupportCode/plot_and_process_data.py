#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:18:45 2018

@author: Teng Ma
"""

def plotAnnaulExits(filename):
    '''
    Variation of annual exits
    Plot a line chart to show the variation of the annual exits from 1973 to 2018
    
    Input-
    filename: BART_Ridership_FY73_FY18.xlsx Make sure the path is right!
    
    '''
    # Import libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # Asserts
    assert isinstance(filename,str),"Pass a valid file"
    #data
    yearlyDataAll = pd.read_excel(filename, header = 1, index_col = 0, skipfooter = 2)
    totalAnnualExits = yearlyDataAll['Total Annual Exits']   
    #plot
    x = totalAnnualExits.index.values
    y = totalAnnualExits
    plt.figure(figsize=(12,8))
    plt.plot(x, y)
    plt.xlabel('Year', fontsize=20)
    plt.ylabel('Counts', fontsize=20)
    plt.xticks(np.arange(1973, 2018+1, (2018+1-1973)//10))
    plt.title('The annual exits of BART from 1973 to 2018', fontsize=20)
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
#    plt.savefig('/Users/teng/OneDrive/ece143/project/result/Annual_exits_Of_BART.png')
    plt.show();
    
# In[]

def growthOfWeekdayAndWeekend(filename):
    '''
    Difference between weekday and weekends for overall usage
    Plot a line chart to show the variation of the average exits of weekday and weekends from 1973 to 2018
        
    Input-
    filename: file path to BART_Ridership_FY73_FY18.xlsx Make sure the path is right!
    
    '''
    # Import libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # Asserts
    assert isinstance(filename,str),"Pass a valid file"
    #data
    yearlyDataAll = pd.read_excel(filename, header = 1, index_col = 0, skipfooter = 2)
    
    #growth of exits for weekday and weekend
    averageWeekdayExits = yearlyDataAll.loc[1989:2017,'Average Weekday Exits']
    averageSaturdayExits = yearlyDataAll.loc[1989:2017,'Average Saturday Exits']
    averageSundayExits = yearlyDataAll.loc[1989:2017,'Average Sunday Exits']
    
    plt.figure(figsize=(12,8))
    plt.title('The average exits of BART from 1989 to 2018')
    x = averageWeekdayExits.index.values
    y1 = averageWeekdayExits
    plt.plot(x, y1, color='green', label='average Weekday Exits')
    z1 = np.polyfit(x, y1, 1)
    p1 = np.poly1d(z1)
    plt.plot(x,p1(x),"r--")
    
    y2 = averageSaturdayExits
    plt.plot(averageSaturdayExits.index.values, y2, color='red', label='average Saturday Exits')
    z2 = np.polyfit(x, y2, 1)
    p2 = np.poly1d(z2)
    plt.plot(x,p2(x),"r--")
    
    y3 = averageSundayExits
    plt.plot(averageSundayExits.index.values, y3, color='blue', label='average Sunday Exits')
    z3 = np.polyfit(x, y3, 1)
    p3 = np.poly1d(z3)
    plt.plot(x,p3(x),"r--")
    
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Counts')
    plt.xticks(np.arange(1989, 2017+1, (2017+1-1989)//9))
#    plt.savefig('/Users/teng/OneDrive/ece143/project/result/The average exits of BART from 1989 to 2017.png')
    plt.show()
    
# In[]  plot Entries of each statin for weekend vs weekday
def plotWeekendVsWeekdayOf(path, stn = 'RM',door='Entries'):
    '''
    
    Difference between weekday and weekends for individual station
    Plot a line chart to show the variation of the average exits or entries of weekday and weekends for individual station from 1973 to 2018
    
    input:
    stn: name of the station with 2 letter
    path: file path to the data folder
    door: should be 'Entries' or 'Exits'
    
    '''
    # Import libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # Asserts
    assert stn in ['RM', 'EN', 'EP', 'NB', 'BK', 'AS', 'MA', 19, 12, 'LM', 'FV', 'CL', 
       'SL', 'BF', 'HY', 'SH', 'UC', 'FM', 'CN', 'PH', 'WC', 'LF', 'OR', 'RR',
       'EM', 'MT', 'PL', 'CC', 16, 24, 'GP', 'BP', 'DC', 'CM', 'CV', 'ED',
       'WP','SS', 'SB', 'SO', 'MB', 'WD', 'OA', 'WS']
    assert isinstance(path,str),"Pass a valid path"
    assert door in ['Entries', 'Exits']
    filename = path + 'result/monthly data by station/' + str(stn) + '_monthly'+ door + 'Data.xlsx'
    yearlyDataAll = pd.read_excel(filename, sheet_name=[0, 1, 2], header = 0, index_col = 0,)

    averageWeekday = yearlyDataAll[0].mean().dropna()
    averageSaturday = yearlyDataAll[1].mean().dropna()
    averageSunday = yearlyDataAll[2].mean().dropna()
    ind = averageWeekday.index.values
    
    plt.figure(figsize=(12,8))
    
    
    plt.plot(averageWeekday.index.values, averageWeekday, color='green', label='average Weekday')
    plt.plot(averageSaturday.index.values, averageSaturday, color='red', label='average Saturday')
    plt.plot(averageSunday.index.values, averageSunday, color='blue', label='average Sunday')
    
    
    # fit the curves
    x = averageWeekday.index.values
    y1 = averageWeekday
#     plt.plot(x, y1, color='green', label='average Weekday Exits')
    z1 = np.polyfit(x, y1, 1)
    p1 = np.poly1d(z1)
    plt.plot(x,p1(x),"r--")

    y2 = averageSaturday
#     plt.plot(averageSaturdayExits.index.values, y2, color='red', label='average Saturday Exits')
    z2 = np.polyfit(x, y2, 1)
    p2 = np.poly1d(z2)
    plt.plot(x,p2(x),"r--")

    y3 = averageSunday
#     plt.plot(averageSundayExits.index.values, y3, color='blue', label='average Sunday Exits')
    z3 = np.polyfit(x, y3, 1)
    p3 = np.poly1d(z3)
    plt.plot(x,p3(x),"r--")

    
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Counts')
    plt.title('The average ' + door + ' of '+ str(stn) + ' from '+ str(ind[0]) +' to 2018')
    
    
    if len(ind)> 10:
        plt.xticks(np.arange(ind[0],ind[-1]+1,2))
    else:
        plt.xticks(np.arange(ind[0],ind[-1]+1,))
    
#    plt.savefig('/Users/teng/OneDrive/ece143/project/result/wekayVsWekend/' + str(stn) + '_Entries.png')
    plt.show()
    
# In[]
    

def extractDataOfEachStation(path, stn = 'RM',door='Entries'):
    '''
    
    extract montly Data of one Station for one door and save in one .xlsx
    
    input:
    stn: name of the station
    path: file path to the data folder
    door: should be 'Entries' or 'Exits'
    
    '''
    # Import libraries
    import collections
    import pandas as pd
    import os  
    # Asserts
    assert stn in ['RM', 'EN', 'EP', 'NB', 'BK', 'AS', 'MA', 19, 12, 'LM', 'FV', 'CL', 
       'SL', 'BF', 'HY', 'SH', 'UC', 'FM', 'CN', 'PH', 'WC', 'LF', 'OR', 'RR',
       'EM', 'MT', 'PL', 'CC', 16, 24, 'GP', 'BP', 'DC', 'CM', 'CV', 'ED',
       'WP','SS', 'SB', 'SO', 'MB', 'WD', 'OA', 'WS']
    assert isinstance(path,str),"Pass a valid path"
    assert door in ['Entries', 'Exits']
    
    year_width = range(2001,2019)
    month_width = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                   'August', 'September', 'October', 'November', 'December']
    month_dic = {'January': '01', 'February':'02', 'March':'03', 'April':'04', 
                 'May':'05', 'June':'06', 'July':'07', 'August':'08', 
                 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    sheetName = {0:'Weekday OD', 1: 'Saturday OD', 2:'Sunday OD'}
    

    Result = collections.OrderedDict()
    for i in range(3):
        Result[i] = pd.DataFrame(index = month_width, columns = year_width)
        
    year = 2008
    month = 'August'
    for year in year_width:
        for month in month_width:
            if year== 2018 and month == 'November':
                break
            monthnum = month_dic[month] 
            file_path = path + 'ridership_' + str(year) + '/Ridership_' + str(year) + monthnum + '.xls' 
            if year>=2010:
                file_path = path + 'ridership_' + str(year) + '/Ridership_' + str(year) + monthnum + '.xlsx' 
            
                 
            df = pd.read_excel(file_path, sheet_name=[0, 1, 2], header = 1,)
            if door == 'Exits':
                if stn not in df[0].index.values:
                    continue
                for i in range(3):
                    Result[i].loc[month,year] = df[i]['Exits'][stn]
            
            elif door == 'Entries':
                if stn not in df[0].columns.values:
                    continue
                for i in range(3):
                    Result[i].loc[month,year] = df[i].loc['Entries'][stn]
        
        
    if not os.path.exists(path + 'result/monthly data by station'):
        os.makedirs(path + 'result/monthly data by station')
    writer = pd.ExcelWriter(path + 'result/monthly data by station/' + str(stn) + '_monthly' + door + 'Data.xlsx')
    for writei in range(3):
        Result[writei].to_excel(writer, sheet_name = sheetName[writei])
    writer.save()
    
# In[] folio map for entry/exit for over year
def plotUsageOfFolioMap(path, year = 2001, door = 'Entries'):
    '''
    
    plot FolioMap of specific year and door  
    
    input:
    stn: name of the station
    path: file path to the data folder
    year: should be one of from 2001 to 2018
    door: should be 'Entries' or 'Exits'
    
    return:
    bart_map: the file of FolioMap
    
    '''  
    # Import libraries
    import pandas as pd
    import folium
    # Asserts
    assert year in range(2001, 2019)
    assert isinstance(path,str),"Pass a valid path"
    assert door in ['Entries', 'Exits']
        
    stations = ['RICH','DELN','PLZA','NBRK','DBRK','ASHB','MCAR','19TH','12TH','LAKE',
                'FTVL','COLS','SANL','BAYF','HAYW','SHAY','UCTY','FRMT','CONC','PHIL','WCRK','LAFY',
                'ORIN','ROCK','WOAK','EMBR','MONT','POWL','CIVC','16TH','24TH','GLEN','BALB',
                'DALY','COLM','CAST','DUBL','NCON','PITT','SSAN','SBRN','SFIA','MLBR','WDUB',
                'OAKL','WARM','ANTC','PCTR'] 
    stn_filename = path + 'Station_Names.xls'
    
    stn_data = pd.read_excel(stn_filename, index_col=0, header=0)
    
    bart_map = folium.Map(location=[37.7983262, -122.1211035], zoom_start=10, tiles="CartoDB dark_matter")
#    year_width = range(2001,2019)
#    year = 2016
    for STN in stations:
    #         print(STN)
        stn = stn_data.loc[STN]['Two-Letter Station Code']
        stationData = path + 'result/monthly data by station/'+ str(stn) + '_monthly' + door + 'Data.xlsx'
        yearlyDataAll = pd.read_excel(stationData, header = 0, index_col = 0,)
        val = yearlyDataAll[year].mean()

        # set up map
        clr=stn_data.loc[STN]['Hex Color'] 
        rd = val/600 

        marker = folium.CircleMarker(location=(stn_data.loc[STN]['Latitude'],
                                               stn_data.loc[STN]['Longitude']),
                                     radius = rd, color = clr, fill=True).add_to(bart_map)
#    bart_map.save('/Users/teng/OneDrive/ece143/project/result/yearly map/' + str(year) + 'ExitsMap.html')
    bart_map
    return bart_map


