#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 03:39:24 2017

"""
import pandas as pd

jocker = pd.read_csv('jockers.txt', sep='\s+', header=None).T
jocker.set_index(0, inplace=1)
jocker['frequency']=0

text = pd.read_excel('Turbulent flow_Stopwords Count.xlsx')
result = pd.DataFrame({})



column={}
column[0] = ' '.join(text.chunk.tolist())
column[1] = ' '.join(text['chunk.1'].tolist())

d={}
for i in range(2):
    d[i] = jocker.copy()
    word_bag = column[i].split()
    for word in word_bag:
        if word in d[i].index:
            d[i].ix[word].frequency += 1
            
    d[i] = d[i][d[i].frequency!=0]
    
    d[i].frequency.sort_values(ascending=False).to_csv('col_{}_stop_stats.csv'.format(i))
