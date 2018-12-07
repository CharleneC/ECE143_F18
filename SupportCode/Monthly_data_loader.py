#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun Joseph
"""

def monthly_data_loader(data_loc,*,verbose=True,load_sheet=0):
	'''
	Reads all the monthly data files and combines all of them to a single dataFrame
	
	Args:
		data_loc (str) : file path to the data folder
	Kwargs:
		verbose (bool) : Set to True to find progress
		load_sheet(int): set to 0 for weekdays, 1 saturday and 2 for sunday
		
	Retruns:
		df (DataFrame) : combined dataFrame
	'''
	# Import libraries
	import pandas as pd
	import numpy as np
	import glob 
	
	# Asserts
	assert isinstance(data_loc,str),"Please enter a valid path"
	assert isinstance(load_sheet,int) and (load_sheet<3 and load_sheet>=0),"set to 0 for weekdays, 1 saturday and 2 for sunday"
	
	# Look up all files under data_loc
	file_list = sorted(glob.glob(data_loc+'/ridership_*/*.xls*'))
	assert len(file_list),"Location specified is empty"
	
	# Create the data frame
	full_data = pd.DataFrame()
	month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
				  'August', 'September', 'October', 'November', 'December']
	
	# Iterate through all the files
	for n,file_ in enumerate(file_list):
		if(verbose):
			print(f"Processing file ({n+1}/{len(file_list)})")
		data=pd.read_excel(file_,skiprows=1,sheetname=load_sheet)
		# Find location of Exits since this would be different for different files
		loc=list(data.columns.values).index('Exits')
		data_selected=data.iloc[:loc-1,:loc]
		# Convert from wide to tall 
		data_selected=data_selected.melt(id_vars='Unnamed: 0',value_name='Rides')
		# Rename 
		data_selected= data_selected.rename(columns={'Unnamed: 0':'Start','variable':'End'})
		#find month
		data_selected['month'] = n%12
		data_selected['Month'] = month_lst[n%12]
		#find year
		data_selected['year'] = 2001+n//12
		full_data = full_data.append(data_selected)
	
	return full_data