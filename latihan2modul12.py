#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:03:31 2022

@author: sonyaridesia
"""

import pandas as pd

df = pd.read_csv('Negara.csv', index_col=0)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print("File Berhasil Dibuat")