#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:56:49 2019

@author: georgiabaltsou
"""


import csv
import os
import networkx as nx


#def weightedFiles(myFile, GTC, graph):
#    #creation of weighted files from different seed each time
#    for index, i in enumerate(GTC):
##        FileAdj(myFile, i)
#        FilesAdj(myFile, i, GTC, index, graph)



#def weightedFiles(myFile, seed, GTC, graph):
#    #creation of weighted files from different seed each time
#    #for index in enumerate(GTC):
#    FilesAdj(myFile, seed, GTC, graph)

#def FileAdj(myFile, s):
#
#    counter = 1
#        
#    #change counter to <=10 for more weights
#    while(counter<=10):
#    
#        with open(myFile) as data_file: 
#            reader = csv.reader(data_file, delimiter=';')        
#            with open('weighted/'+str(myFile)+'<'+str(s)+'-'+' '+'>'+str(counter)+'.csv', 'a') as out_file:
#                writer = csv.writer(out_file, delimiter=';')
#                
#                for row in reader:
#                    w = 1
#                    if ((row[0] == s) or (row[1] == s)):
#                        w *= counter  
#                    writer.writerow([row[0],row[1], w])
#                    
#                counter += 1
                                      
                    
#def FilesAdj(myFile, s, GTC, index, graph):
#def FilesAdj(myFile, s, GTC, graph):
#                                     
##    for j in GTC[index:]: 
#    for j in GTC:
#        
#        if (s==j) or ((j, s) not in graph.edges()): continue
##        if s==j: continue
#    
#        counter2 = 2
#        #change counter to <=10 for more weights
#        while(counter2<=6):
#            
##            if counter2 == 1:
##                counter2 += 1
##                continue
#
#            with open('lfr/'+str(myFile)) as data_file: 
#                reader = csv.reader(data_file, delimiter=';')
#                
#                os.chdir('weighted/')
#                
#                with open(str(myFile)+'<'+str(s)+'-'+str(j)+'>'+str(counter2)+'.csv', 'a') as out_file:
#                    writer = csv.writer(out_file, delimiter=';')
#                        
#                    
#                    for row in reader:
#                        w = float(row[2])
#                        #if ((row[0] == s) or (row[1] == s) or (row[0] == j) or (row[1] == j)):
#                        if ((row[0] == s) or (row[1] == s)):
#                            w *= counter2 
#                        writer.writerow([row[0],row[1], w])
#                            
#                    counter2 += 2 
#
#                os.chdir('../')                      
                        

def FilesAdj(myFile, s, GTC, graph):
                                     
 
    for j in graph.neighbors(s):
        
        #if (s==j) or ((j, s) not in graph.edges()): continue

    
        counter2 = 2
        #change counter to <=10 for more weights
        while(counter2<=6):
            

            with open('lfr/'+str(myFile)) as data_file: 
                reader = csv.reader(data_file, delimiter=';')
                
                os.chdir('weighted/')
                
                with open(str(myFile)+'<'+str(s)+'-'+str(j)+'>'+str(counter2)+'.csv', 'a') as out_file:
                    writer = csv.writer(out_file, delimiter=';')
                        
                    
                    for row in reader:
                        w = float(row[2])

                        if ((row[0] == s) and (row[1] == j)) or ((row[1] == s) and (row[0] == j)):
                            w *= counter2 
                        writer.writerow([row[0],row[1], w])
                            
                    counter2 += 2 

                os.chdir('../')                  
                        
                        
                        
def FilesAdjAll(myFile, s, GTC, graph): 
    
    
        
        #if (s==j) or ((j, s) not in graph.edges()): continue

    
        counter2 = 2
        #change counter to <=10 for more weights
        while(counter2<=6):
            

            with open('lfr/'+str(myFile)) as data_file: 
                reader = csv.reader(data_file, delimiter=';')
                
                os.chdir('weighted/')
                
                with open(str(myFile)+'<'+str(s)+'-'+str(s)+'>'+str(counter2)+'.csv', 'a') as out_file:
                    writer = csv.writer(out_file, delimiter=';')
                        
                    
                    for row in reader:
                        w = float(row[2])
                        for j in graph.neighbors(s):

                            if ((row[0] == s) and (row[1] == j)) or ((row[1] == s) and (row[0] == j)):
                                w *= counter2 
                        writer.writerow([row[0],row[1], w])
                            
                    counter2 += 2 

                os.chdir('../') 
                        
                        
            









            
                        