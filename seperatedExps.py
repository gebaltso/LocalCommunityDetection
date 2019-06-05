#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:10:01 2019

@author: georgiabaltsou

Run seperated examples for unweighted, reweighted etc graphs
"""

import csv
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import random
import time
import sys
import shutil
from lemon import lemon
from lte import lte
from tce import tce 
from newLCD import newLCD
from metrics import metrics
from fileWeightAdjacement import FilesAdj, FilesAdjAll
from LFR import LFR
from ReWeighting import reWeighting

start_time = time.time()

os.chdir('seperatedExps/datasets/lfr/')

myFile = 'lfrEdgelistN1000MU0.1*.csv'
file = 'lfrEdgelistN1000MU0.1*'

G = nx.Graph()
G = nx.read_weighted_edgelist(myFile, create_using=nx.Graph(), delimiter=";", encoding='utf-8-sig')

#plt.axis('off')         
    
#sxediasmos grafou
#nx.draw(G, node_size=100,  with_labels=True, font_size=10)

#call reWeighting for find new weights for the graph's edges
#ReWeigthedFile, graph = reWeighting(myFile)
#
#print("Re-Weighting of edges done.")
#print("------------------------------")
#
#shutil.copy2(myFile, 'lfrEdgelistN1000MU0.1*.csv<111-111>1.csv')
#shutil.copy2('lfrEdgelistN1000MU0.1*.csv<111-111>1.csv','../reweighted/lfrEdgelistN1000MU0.1*.csv<111-111>1.csv' )
#shutil.copy2(myFile, '../reweighted/lfrEdgelistN1000MU0.1*.csv<000-000>1.csv')

GTC = ['327', '210', '352', '485', '616', '236', '371', '501', '246', '638', '639']

##find the length of the community stored in GTC
trueComm = len(GTC)


os.chdir('../')

#seed = '485'

for seed in GTC:
    FilesAdj(myFile,seed, GTC, G)
    FilesAdjAll(myFile,seed, GTC, G)


#FilesAdj(myFile,seed, GTC, G)
#FilesAdjAll(myFile,seed, GTC, G)

#print(list(G.neighbors('485')))

#for seed in GTC:
#    if(seed=='485'):
#        FilesAdj(myFile,seed, GTC, G)
#    else:
#        continue

#weightedFiles(myFile, GTC, G)

print("Weighted files created.")
print("------------------------------")

#sys.exit()

#print("Current Working Directory " , os.getcwd())
#
#os.chdir('../')

for filename in os.listdir('weighted'):
    for seed in GTC:
        
#        if  seed=='485' :
            
    #   lemon('weighted/'+str(filename), seed, file)
            
            lte('weighted/'+str(filename), seed, file)
    
            tce('weighted/'+str(filename), seed, file)
           
            newLCD('weighted/'+str(filename), seed, file)
        

print("Algorithms completed.")
print("------------------------------")

os.chdir('communities')


for filename in os.listdir(os.getcwd()):
    
    
    if not filename.startswith('.'):
    
        algorithm = filename.split("_")[0]
        
        metrics(str(filename), GTC, trueComm, algorithm)


print("Execution time: %s seconds " % (time.time() - start_time))
print("------------------------------") 






###############################################################################








#
#
#
###call reWeighting for find new weights for the graph's edges
#ReWeigthedFile, graph = reWeighting(myFile)
#
#print("Re-Weighting of edges done.")
#print("------------------------------")
#
###till now working dir = /Users/georgiabaltsou/Desktop/PhD/Local_exp/experiments/datasets/lfr
#print("Current Working Directory " , os.getcwd())
#
#
#os.chdir('../')
#
#weightedFiles(ReWeigthedFile, GTC, graph)
#
#print("Weighted files created.")
#print("------------------------------")
#
##sys.exit()
#
#for filename in os.listdir('weighted'):
#    for seed in GTC:
#        
##        lemon('weighted/'+str(filename), seed, file)
#        
#        lte('weighted/'+str(filename), seed, file)
#
#        tce('weighted/'+str(filename), seed, file)
#       
#        newLCD('weighted/'+str(filename), seed, file)
#        
#print("Algorithms completed.")
#print("------------------------------")
#
#
###Write the files with precision and recall for each community of the 3 algorithms
#
#os.chdir('communities')
#
#
#for filename in os.listdir(os.getcwd()):
#    
#    
#    if not filename.startswith('.'):
#    
#        algorithm = filename.split("_")[0]
#        
#        metrics(str(filename), GTC, trueComm, algorithm)
#        
#    
#print("Metrics files created.")
#print("------------------------------")
#
#print("Execution time: %s seconds " % (time.time() - start_time))
#print("------------------------------")   