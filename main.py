#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:17:17 2020

@author: anhnguyen
"""

#Import needed libraries
import pandas as pd
from datetime import datetime, timedelta

#Read the file
log1 = pd.read_csv("steps.txt", names = ['Dist'])

#Define function fit_tracker() to get the output
def fit_tracker():
    global table
    date= []
    start = datetime(2019,1,1)
    #Calculate date
    for i in list(log1.index):
        date.append(start + timedelta(days=i))       
    log1['Date'] = date
    output = pd.DataFrame(columns = ["Month", "Total", "Average", "Minimum", "Maximum"])
    #Find sum
    output['Total'] = log1.resample('M', on='Date')['Dist'].sum()
    #Find mean
    output['Average'] = round(log1.resample('M', on='Date')['Dist'].mean(),2)
    #Find min
    output['Minimum'] = log1.resample('M', on='Date')['Dist'].min()
    #Find max
    output['Maximum'] = log1.resample('M', on='Date')['Dist'].max()
    #Months
    output['Month'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #Display output
    print(output)
    
fit_tracker()
