'''
DEGROOT LEARNING MODEL

Script to functionalize Degroot Learning Model

Inputs: 
  T (python type: Numpy Matrix)- weighted adjacency Matrix
  b (python type: Numpy Matrix) - values of individuals initial beliefs at t = 0
  n (python type: Integer) - number of updates/iterations - Default Value = 10
  
Output: 
  Updated adjacency matrix
  Updated graph (? NOTE TO SELF: UNSURE - MAY TAKE OUT)

Model: 
  Individuals - 1,2,...n
  T weighted directed network
  Stochastic Matrix
  
  Start with beliefs b_i(0) in [0,1]
  Updating b_i(t) = SUM(T_(i,j)b_j(t-1))
    update is a weighted average of the belief of the neighbors which is captured by T_(i,j)
    SUM(T_(i,j)) = 1 wh ere T_(i,j) >= 0 
'''

import networkx as nx
import numpy as np

def degroot(T,b,n=10):
  G = nx.from_numpy_matrix(T, parallel_edges=False, create_using=nx.DiGraph)
  T2 = T
  for i in range(n):
    b = T.dot(b)
    T2 = T.dot(T2)
  return T2,G,b
