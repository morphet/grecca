""" This helper extracts all data from the pitrading cd, flattens the dir structure, and appends
a 2 letter category code at the start of the symbol"""

import numpy as np
import pandas as pd
import zipfile
import os



# open data directories, and create a dictionary of locations.
# the keys are tyXXX wher ty is the type of asset
hist_data_location = "/home/alt/pitrading/"
all_path=hist_data_location+'all/'

prefixes={"Dow Jones Industrial Components":"dj","Forex":"fx","Indicators":"id","Stocks":"st","ETFs":"ef","Futures":"fu","Indices":"in"}
data_catalog={}
for i in os.listdir(hist_data_location):
	if i != 'all':
		for j in os.listdir(hist_data_location+"/"+i):
			data_catalog[prefixes[i]+j.strip(".zip")] = hist_data_location+i+"/"+j
		
#~ Extract all 
subjects=["efQQQ","efDIA","fxEURUSD"]
for i in data_catalog:
	print data_catalog[i]
	a = zipfile.ZipFile(data_catalog[i])

	a.extract(a.namelist()[0],path=all_path)
	os.rename(all_path+a.namelist()[0],all_path+i+'.txt')
