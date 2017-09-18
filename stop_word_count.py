#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:34:31 2017

@author: dt
"""

import pandas as pd

jocker = pd.read_csv('jockers.txt', sep='\s+', header=None).T

text = pd.read_excel('Turbulent flow_Stopwords Count.xlsx')
result = pd.DataFrame({})

jocker.set_index(0, inplace=1)
jocker['frequency']=0

for key, row in text.iterrows():
    d={}
    for i in [0,1]:
        d[i] = jocker.copy()
        print(key)
        word_bag = row[i].split()
        for word in word_bag:
            if word in d[i].index:
                d[i].ix[word].frequency += 1

        d[i] = d[i][d[i].frequency!=0]
    result = result.append([[sum(d[0].frequency), len(d[0]),sum(d[1].frequency), len(d[1])]])
        
result.columns=['sum1','distinct1','sum2','distinct2']
result.index = range(len(result))

result.to_csv('stop_words_count.csv',index=False)