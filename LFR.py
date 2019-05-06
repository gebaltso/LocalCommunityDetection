#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:45:49 2018

@author: georgiabaltsou
"""

#https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.community_generators.LFR_benchmark_graph.html#networkx.algorithms.community.community_generators.LFR_benchmark_graph

#Produces non-overlapping communities

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import LFR_benchmark_graph
import csv

n = 1000 #(int)number of nodes
tau1 = 3  #(float) Power law exponent for the degree distribution of the created graph. This value must be strictly greater than one.
tau2 = 1.1  #(float) Power law exponent for the community size distribution in the created graph. This value must be strictly greater than one.
mu = 0.1  #(float) Fraction of intra-community edges incident to each node. This value must be in the interval [0, 1].

#greater mu => pio asafeis koinothtes!


#average_degree and min_degree  must be in [0, n]. One of these must be specified.
#max_degree if not specified is set to n.
#min_community if not specified is set to min_degree.
#max_community if not specified is set to n.
#tol(float) Tolerance when comparing floats, specifically when comparing average degree values.
#max_iters (int) Maximum number of iterations to try to create the community sizes, degree distribution, and community affiliations.
#seed (integer, random_state, or None (default)) Indicator of random number generation state.

G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=10, max_degree=50, min_community=10, max_community=50)

#na mh sxediazontai oi aksones    
#plt.axis('off')         

#sxediasmos grafou
#nx.draw(G) 

communities = {frozenset(G.nodes[v]['community']) for v in G}

adjacency_list_filename = "lfrAdjlistExample.txt"
edge_list_filename = "lfrEdgelistExample.txt"
community_list_filename = "lfrCommunity.txt"

#print('Communities: ', communities)

with open('lfrCommunitiesExample.txt', 'w') as fc:
    fc.write(str([list(x) for x in communities]))


nx.write_adjlist(G,adjacency_list_filename)
fh=open(adjacency_list_filename,'wb')
nx.write_adjlist(G, fh)



edge_list = []
with open(adjacency_list_filename, 'r') as f:
    for line in f:
        
        if line.startswith("#"): #skip first comment lines
            continue;
        else:

            line = line.rstrip('\n').split(' ')
            source = line[0]
            for target in line[1:]:
                #edge_list.append("%s %s 1" % (source, target)) #1 is for the weight
                edge_list.append("%s %s" % (source, target))

with open(edge_list_filename, 'w') as f:
    f.write('%s\n' % ('\n'.join(edge_list)))
    
  
with open(community_list_filename, 'w') as f:
    for item in communities:
        f.write("%s\n" % str(list(item)))
        
with open(community_list_filename, 'r') as my_file:
    text = my_file.read()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace(",", "")
    
with open(community_list_filename, 'w') as my_file:
        
    my_file.write(text)

#convert edge txt file to csv file appending also weight 1 to all edges
with open('lfrEdgelistExample.txt') as data_file: 
            reader = csv.reader(data_file, delimiter=' ')        
            with open('lfrEdgelistExample.csv', 'w') as out_file:
                writer = csv.writer(out_file, delimiter=';')  
                for row in reader:
                    writer.writerow([row[0],row[1], 1])







