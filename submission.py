from copy import copy, deepcopy
import sys, os
import numpy as np

# Name: Yousif Alnai
# PID: 

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################
def myBranchBound(C):
    '''
    Implement Assignment Branch and Bound function under here.
    Some Helper functions that might help you modularize the code:
        - upper_bound(A, X) : calculates upper bound at node X
        - lower_bound(A, X) : calculates lower bound at node X
        - SNH(A) : calculates Smallest Number Hueristic of a Matrix
        - rowMin(A) : calculates Row-Min strategy Lower bound of a Matrix
        - minElement(A) : calculates minimum element in an array with its position
        - calcMatrixMinor(A, i, j) : calculates minor of a Matrix at a given location
    Note: These functions are recommended however we won't be grading your implementations of the
          above stated functions

    Input:
    C: (N x N) with c_ij representing the time taken by agent i to complete task j - list[list[int]]

    Input constraints: 2<N<10

    return:
    X:  Optimal Assignment of Jobs -  list[list[int]]
    ub_list: List of upper bound values at which they were updated(0th index should be the first upper bound calculated by SNH) - list[int]
    node_count: Number of nodes evaluated by your branch and bound algorithm - int
    
    '''
    pass

#######################################################
##############       QUESTION 2 HERE   ################
#######################################################
def myDynamicProgramming(n,c, V, W):
    '''
    Implement Knapsack Dynamic Programming function under here.

    Input:
    n: Number of items - int
    c: Capacity of the Knapsack - int
    V: List of Values of each item - list[int]
    W: List of Weights of each item - list[int] 

    return:
    Z: Optimal choice of items for the given constraints - list[int] 
    DP: Dynamic Programming table generated while calculation - list[list[int]]
    
    '''
    pass

