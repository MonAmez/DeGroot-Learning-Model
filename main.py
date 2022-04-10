'''
Main Script for Degroot Learning Model

T is the adjacency matrix used to create a 
weighted directed network

N is the number of updates/iterations desired to use in the model

b = Initial beliefs of the individuals
'''
import numpy as np
import degroot as dg
import imp
import matplotlib.pyplot as plt
imp.reload(dg)

b=np.array([1,0,1])
b=b.reshape(3,1)
print(b)
T = np.array([[0,0.5,0.5],[1,0,0],[0,1,0]])

T,G,p = dg.degroot(T,b,100)
print(p)
#Visualize Graph
plt.figure()

#Graph Attributes
layout = nx.circular_layout(G)
nx.draw(G, layout, with_labels=True, node_size = 1000)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,layout,edge_labels=labels)

#Show Figure
plt.show()




