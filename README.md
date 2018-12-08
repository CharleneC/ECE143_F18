# ECE143_F18
Repository for ECE143 Project

##  Note to evaluators 
Due to the nature of some of the libraries used and the interactive nature of some of the outputs a lot of them cannot be seen natively in ipynb file please check the assosiated Results and also the ppt for complete outputs.



#### Requirements to run the current project
- Data please use this link to download the data and save it in the working directory after extacting it (link :https://drive.google.com/file/d/1HmISwXIPAD7THDOPpydNKxobYYrH_3H8/view?usp=sharing)

- Dependencies
	- Numpy : 1.14.2
	- Pandas : 0.22.0
	- Seaborn: 0.9.0
	- Bokeh : 0.12.13
	- Matplotlib : 2.1.2
	- Folium: 0.6.0
	- Glob : 0.6
	- Ipysankeywidget : 0.2.4
	- PyeCharts : 0.5.11
	
to install Dependencies please run
```bash
pip install -r requirements.txt
```

#### Data cleaning 
- [x] renaming all files to have consitant formatting
- [x] convert 214 files to single tall format
- [ ] make functions modular so that reads the correct file and extracts the correct info for the each hourly data files

#### things to extract from each data source
**hourly**
- [X] hourly variations
- [X] most busy days

**monthly averages**
- [X] variation of rideship over years
- [X] variation with months

#### Plots 
- [X] hourly ridership entry/exit (line chart/ kde) - Charlene
- [X] 2 most popular and 2 least popular - Arun
- [X] week end vs weekday over the years - Tim 
- [X] pie charts for station trafic for  selected years - Jiaqi
- [X] folio map for hourly for one day  - Charlene
- [X] folio map for entry/exit for over year - Tim
- [X] top ten most ridden days and least ridden days - compare to actual events -Arun 
- [X] variation of rideship based on day of the week - Arun


#### questions answered
- [X] overall growth (+prdictions)
- [X] daily breakdown 
- [X] rush hour analys
- [X] possible stations to add
