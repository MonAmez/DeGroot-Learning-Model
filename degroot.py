'''
DEGROOT LEARNING MODEL

Script to functionalize Degroot Learning Model

Inputs: 
  T - weighted adjacency Matrix
  Number of Updates - Default Value = 10
  
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
    SUM(T_(i,j)) = 1 where T_(i,j) >= 0 
'''

def degroot(T,n=10):
  return T


