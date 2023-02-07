# -*- coding: utf-8 -*-
 
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

def remove_mean(data):
    return data-np.mean(data)

def add_number(data, number):
    return data+number 

def read_tables(filename):
    return pd.read_csv(filename,header=2).dropna(subset=['Nombre'])

def prices(tickers,start_date, end_date, fechas_consulta):
    
    matriz = yf.download(tickers, start = start_date, end = end_date)['Close']
    matriz = matriz.reset_index()    
    matriz["Coincidencia"] = False

    for i in (fechas_consulta):
        for j in range(len(matriz)):
            if (matriz["Date"][j]) ==  i:
               matriz["Coincidencia"][j] = True  
    
    final=matriz[matriz['Coincidencia'] == True]
    final.drop(['Coincidencia'], axis=1, inplace=True)
    
    return final