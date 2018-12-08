# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:16:13 2018

@author: Jiaqi Yan, Teng Ma
"""

def create_sankey_traffic_flow(filename):
    '''
    Create sankey diagram to visualize traffic flow among stations in starting 
    and ending on the date given. 
    
    Input:
        Date :given in day,month,year.(User provided)
        starting: List of four letter code strings that traffic flow start from.(User provided)
        ending: List of four letter code strings that traffic flow end at.(User provided)
        filename: hourly data file. Make sure the years are equal.(User provided)
        
    Output:
        Opens svg daigram in browser.
        
    '''
    
    assert isinstance(filename,str)
    
    #import libraries
    import pandas as pd
    import collections
    from ipysankeywidget import SankeyWidget
    #---
    starting = ['EMBR','CIVC','MONT','POWL','12TH']
    ending = ['DUBL','BALB','24TH','PHIL','DELN','WCRK','FRMT']
    year = 2018
    month = 8
    day = 22
    
    #read data
    fo = pd.read_csv(filename, index_col=0, header=None, names=['Date','Hour','Departing','Arriving','Count'])
    #find data on the date given
    fo_find_date = fo.loc['{}-0{}-{}'.format(year,month,day)]

    select_date = collections.OrderedDict()
    for i in starting:
        select_date[i] = fo_find_date[fo_find_date.Departing == i]
    
    #filter data based on starting and ending lists
    specific_start_end = collections.OrderedDict()
    startend_number = {}
    for start in starting:
        for end in ending:
            specific_start_end[start+end] = select_date[start][select_date[start].Arriving == end]
            add_up = 0
            for num in list(specific_start_end[start+end].Count):
                add_up += num
                startend_number[start+end] = add_up
    #create sankey diagram
    traffic_flow = []      
    for key in specific_start_end.keys():
        sankey_dict = {}
        sankey_dict['source'] = specific_start_end[key]['Departing'].iloc[0]    
        sankey_dict['target'] = specific_start_end[key]['Arriving'].iloc[0]
        sankey_dict['value'] = specific_start_end[key]['Count'].sum()
        traffic_flow.append(sankey_dict)
    color = ['grey','darkgrey', 'dimgrey', 'lightgrey','silver']
    for col in color:    
        for element in traffic_flow:
            for i in range(5):
                if element['source'] == starting[i]:
                    element['color'] = color[i]
    s = SankeyWidget(links = traffic_flow,margins=dict(top=0, bottom=0,left=100,right=100))      
    return s
