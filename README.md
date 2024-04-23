# Weisfeiler-Leman Test
Just a simple Weisfeiler-Leman Test. Contains no deviations from original algorithm, unlike all of the other publicly available repositories that we have found.
Graphs are assumed to be undirected. 

Input:
line 1: the number of nodes, n, in the input graphs (which should be the same if they have a chance of being isomorphic)
line 2 ~ n+1: the adjacency matrix of the first input graph (must be symmetric)
line n+2 ~ 2n+1: the adjacency matrix of the second input graph (also symmetric)

Output:
One of the following:
1. We cannot conclude that they are different
2. We can conclude that they are different

Recall that the WL test never says "yes", only "no" or "I don't know."

Example: 
Both graphs in this example are three nodes connected in a line: o-o-o. They differ in that the rows and columns of their adjacency matrices have been permuted. 
Input: 
3
0 1 1 
1 0 0 
1 0 0 
0 1 0
1 0 1 
0 1 0

Output:
We cannot conclude that they are different
