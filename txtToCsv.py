#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:11:18 2019

@author: georgiabaltsou
"""

#convert edge txt file to csv file appending also weight 1 to all edges

import csv


with open('lfrEdgelistExample.txt') as data_file: 
            reader = csv.reader(data_file, delimiter=' ')        
            with open('log.csv', 'w') as out_file:
                writer = csv.writer(out_file, delimiter=';')  
                for row in reader:
                    writer.writerow([row[0],row[1], 1])