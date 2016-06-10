#!/usr/bin/python
import os, sys, csv
import fast_influence_maximization as im
from collections import defaultdict

#Functions to create nodes dictionary
def build_nodes_dict(source_file):
    nodes = defaultdict(dict)
    headers = ['Nd_From', 'Nd_To', 'Propagation_Prb']
    with open(source_file, 'rb') as fp:
        reader = csv.DictReader(fp, fieldnames=headers, delimiter='\t', quoting=csv.QUOTE_NONE, skipinitialspace=True)
        for rowdict in reader:
            if None in rowdict:
                del rowdict[None]
            nd_from = rowdict.pop("Nd_From")
            nd_to = rowdict.pop("Nd_To")
            nodes[nd_from][nd_to] = rowdict
    return dict(nodes)
#*************************** End of Functions ***********************

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
#check number of arguments
if(len(sys.argv) < 4):
	sys.exit("Need to provide 4 arguments: ./benmark.py graph k R")

#parse graph file
graph_file = str(sys.argv[1])
k = int(sys.argv[2])
R = int(sys.argv[3])

#generate nodes dictionary
nodes_dict = build_nodes_dict(graph_file)
"""
writer = csv.writer(open('dict.csv', 'wb'))
for key, value in nodes_dict.items():
   writer.writerow([key, value])
"""
  
#get specific node details
print len(nodes_dict["0"]), len(nodes_dict["1"])
print len(nodes_dict)

####### Seed selection
seeds = im.select_seed(nodes_dict, k, R)
print seeds

""""
for i in 1:k
	print i, '-th seed = ', seeds[i]

"""
