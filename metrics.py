#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:32:29 2019

@author: georgiabaltsou
"""

import os
import csv
import numpy as np
import editdistance


def metrics(myFile, GTC, trueComm, algorithm):
        
    with open(str(myFile), 'r') as in_file:
        reader = csv.reader(in_file, delimiter=';')
        #skip 1st line as its the header line
        next(reader, None)
    
            
        with open('metrics_'+str(myFile), 'a') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            
            if os.stat('metrics_'+str(myFile)).st_size == 0:
                writer.writerow(["ALGORITHM","Node 1","Node 2","Mult Weight", "PRECISION", "RECALL", "F1", "JaccardIndex"])
        
            for row in reader:
                                
                node1 = str(row[0])
                node2 = str(row[1])
                weight = float(row[2])
                
                
                inComm = 0
                obtainedComm = np.unique(row[3:])
                                
                for i in obtainedComm:
                    resultComm = len(obtainedComm)
                    if i in GTC:
                        inComm += 1
                   
                precision = inComm/resultComm
                recall = inComm/trueComm
                if (precision+recall)==0:
                    F1=0
                else:  
                    F1 = 2 * (precision * recall) / (precision + recall)
                
                JI = len(np.intersect1d(GTC, obtainedComm))/len(np.union1d(GTC, obtainedComm))
                
#                ed = editdistance.eval(GTC, obtainedComm)
                
                writer.writerow([algorithm, node1, node2, weight, precision, recall, F1, JI]) 
                

    
    
                    
                