#/user/python/
# encoding: utf-8
"""
This file generates a seed set selection for Influence Maximization usign Monte Carlo methods

"""

#************* functions list goes here to find seeds using Monte Carlo method
def select_seed(nodes_dict, k, R):
    
    size = len(nodes_dict)
    seeds = size
    return seeds