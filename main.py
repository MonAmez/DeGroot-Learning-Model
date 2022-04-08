'''
Main Script for Degroot Learning Model

T is the adjacency matrix used to create a 
weighted directed network

N is the number of updates/iterations desired to use in the model

b = Initial beliefs of the individuals
'''

import numpy as np
import degroot as dg
import matplotlib.pyplot as plt

T = np.matrix('0 .5 .5;1 0 0; 0 1 1')
T,G = dg.degroot(T)

#Visualize Graph
plt.figure()

#Graph Attributes
layout = nx.circular_layout(G)
nx.draw(G, layout, with_labels=True, node_size = 1000)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,layout,edge_labels=labels)

#Show Figure
plt.show()

