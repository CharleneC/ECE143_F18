#@author: Arun Joseph

def plot_station_percent_share(df,*,size='large'):
    '''
    This function plots the variation of percentage share over years for 4 large or small stations

    Args:
        df (dataFrame) : data, should be a valid pandas dataframe

    Kwargs:
        size (str) : valid options large or small

    '''

    #import libraries required
    import seaborn as sns
    import pandas as pd
    from matplotlib import pyplot as plt

    #asserts
    assert isinstance(df,pd.DataFrame),"df should be a valid pandas dataframe"
    assert isinstance(size,str) and (size=='large' or size=='small'),"size should be either set to large or small"

    # data manipulations

    data_station_traffic = df[['Start','year','Rides']].groupby(['Start','year']).sum().reset_index()
    data_station_traffic=data_station_traffic.astype({"Start": str})
    data_station_traffic['Percent_share']=(100*data_station_traffic.Rides)/data_station_traffic.Rides.groupby(data_station_traffic['year']).transform('sum')

    if size =='large':
        large_station_data = data_station_traffic[data_station_traffic.Start.str.contains('EM|CC|PL|MT')]
        g=sns.lineplot(data=large_station_data,x='year',y='Percent_share',hue='Start')
        g.xaxis.set_major_locator(plt.MultipleLocator(1))
        g.figure.set_size_inches(10,8)
        g.set_title('variation of percentage share for top 4 stations')
        g.set_xlabel('Years')
        g.set_ylabel('Percentage Share')

    if size =='small':
        small_station_data = data_station_traffic[data_station_traffic.Start.str.contains('DC|NB|SB|NC')]
        g=sns.lineplot(data=small_station_data,x='year',y='Percent_share',hue='Start')
        g.xaxis.set_major_locator(plt.MultipleLocator(1))
        g.figure.set_size_inches(10,8)
        g.set_title('variation of percentage share for 4 small stations')
        g.set_xlabel('Years')
        g.set_ylabel('Percentage Share')

    plt.show()
