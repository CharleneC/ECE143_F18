#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun Joseph
"""

def weekly_variation_box(data_frame,year=2017):
	'''
	Takes in the data and plots box plot corresponding to chosen year for weekly variation
	
	Args:
		data_frame (DataFrame)     : file path to the data folder
		year (int) [default =2017] : year to plot the trend for
		
	'''
	# Import libraries
	import pandas as pd
	import numpy as np 
	import seaborn as sns
	from matplotlib import pyplot as plt

	
	# Asserts
	assert isinstance(data_frame,pd.DataFrame),"Pass a valid dataFrame"
	assert isinstance(year,int) and year>2000 and year <2019, "Entera valid year between 2001 and 2018"
	
	# Clean Data
	data_daily = data_frame[['Date','Rides']].groupby(['Date']).sum().reset_index().reset_index()
	data_daily['day']=data_daily['index']%7
	
	g = sns.boxplot(data=data_daily,x='day',y='Rides',showfliers=False,palette='Blues_d')
	g.figure.set_size_inches(10,8)
	g.set_title('Variation of Rides with Day of the week')
	g.set_xlabel('Day of the week')
	g.set_ylabel('Rides')
	plt.show()