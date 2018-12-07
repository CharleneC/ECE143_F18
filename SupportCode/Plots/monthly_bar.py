#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun Joseph
"""

def monthly_variation_box(data_frame,year=2017):
	'''
	Takes in the data and plots box plot corresponding to chosen year
	
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
	g = sns.boxplot(data=data_frame[data_frame['year']==year],x='Month',y='Rides',showfliers=False,palette='Blues_d')
	g.figure.set_size_inches(10,8)
	g.set_xticklabels(rotation=30,labels=data_frame.Month.unique())
	g.set_title('Variation of Rides with Months')
	g.set_xlabel('Months')
	g.set_ylabel('Rides')
	plt.show()