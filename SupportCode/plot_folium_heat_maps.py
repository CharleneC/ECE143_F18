#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:16:45 2018

@author: CharleneCuellarVite
"""

def gen_hrly_df(day,month,year,ride_filename,stations):
    '''
    Generate Hourly Departure DataFrame. Used for HeatMap Plotting
    
    Input-
    Date given in day,month,year
    ride_filename = hourly data file. Make sure the years are equal
    stations = list of strings with 4 Letter Station codes
    
    Output-
    Pandas DataFrame covering each station on the given day.
        [Station - Hour - Count]
    '''
    #===Data
    import pandas as pd
    
    data = pd.read_csv(ride_filename, index_col=0, header=None, names = ['Date','Hour','Departing','Arriving','Count'])

    #===
    
    y_m_d = '%d-%.2d-%.2d'%(year,month,day)
    single_day = data.loc[y_m_d] #single out data from a single day
    
    hrly_df = pd.DataFrame(columns = ['Station','Hour','Count']) #set up output
    rw = 0 #selecting row to add data

    for STN in stations:
        #select only those departing at stations STN (STN is a 4 letter code per station)
        dep_stn = single_day.loc[single_day['Departing'] == STN] 

        for t in range(24):
            tme = dep_stn.loc[dep_stn['Hour'] == t]
            val = tme['Count'].sum()
            hrly_df.loc[rw] = [STN,t,val]
            rw = rw +1
    
    return hrly_df

#%% Generate Heatmap
def plot_heatmap(day, month, year,stations, df):
    '''
    This function will generate a heat map depicting departures on the date given.  
    
    Input:
        Date given in day,month,year
        df - df generated from gen_hrly_df()
    Output:
        Open an html file in the browser of the heatmap
    '''
    #Bokeh Plot
    from bokeh.io import show
    from bokeh.models import LinearColorMapper, BasicTicker, PrintfTickFormatter, ColorBar
    from bokeh.plotting import figure
    
    hour = [str(i) for i in range(24)]
    y_m_d = '%.2d-%.2d-%d'%(month,day,year)

    
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors, low=df.Count.min(), high=df.Count.max()/4 ) 
    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
    
    p = figure(title="Hourly Departing Counts for all Stations on %s"%y_m_d.format(0, 23),
               x_range=hour, y_range=stations,x_axis_location="above",
               plot_width=900, plot_height=400,tools=TOOLS, toolbar_location='below',
               tooltips=[('station', '@Station'),('hour', '@Hour'), ('count', '@Count')])
    
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff =0
    p.xaxis.major_label_orientation = 0
    
    p.rect(x="Hour", y="Station", width=1, height=1,source=df,
           fill_color={'field': 'Count', 'transform': mapper},line_color=None)
    
    color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                         ticker=BasicTicker(desired_num_ticks=len(colors)),
                         formatter=PrintfTickFormatter(format="%d"),
                         label_standoff=6, border_line_color=None, location=(0, 0))
    p.add_layout(color_bar, 'right')
    
    show(p)      # show the plot

#%% Plot Map
def plot_map(hour, day, month, year,stations,stn_filename,ride_filename):
    '''
    Given date and hour, draw map of departures at ALL stations.
    
    Input:
        Date given in day,month,year. Specific hour given in hour.
        stn_filename: this filename contains all the 2 and 4 letter codes of each station
                    as well as a color hex code to associate each of them with.
        ride_filename: hourly data file. Make sure the years are equal
        stations: List of 4 letter code strings that will be plotted
    Output:
        Opens html map in browser. Larger circle = more departures

    '''
        
    import pandas as pd
    
    stn_data = pd.read_excel(stn_filename, index_col=0, header=0)
    ride_data = pd.read_csv(ride_filename, index_col=0, header=None)
     
    import folium
    
    #Get total departures from station on date
    y_m_d = '%d-%.2d-%.2d'%(year,month,day)
    single_day = ride_data.loc[y_m_d]
    
    #where to center the map
    bart_map = folium.Map(location=[37.7983262,
                                    -122.1211035],
                                    zoom_start=10,
                                    tiles="CartoDB dark_matter")
    
    for STN in stations:
        #select only those departing at stations STN (STN is a 4 letter code per station)
        dep_stn = single_day.loc[single_day[2] == STN] #column 2 = departing ; column 3 = arriving
        tme = dep_stn.loc[dep_stn[1] == hour]
        val = tme[4].sum()
    
        # set up map
        clr=stn_data.loc[STN]['Hex Color'] 
        rd = int(val/30)+1 #for some reason, a radius of 0 does not give a single point...
  
    
        
        marker = folium.CircleMarker(location=(stn_data.loc[STN]['Latitude'],
                                               stn_data.loc[STN]['Longitude']),
                                     radius = rd, color = clr, fill=True).add_to(bart_map)
    return bart_map

    