#################
#
#   GUIDE
# 1.) Ask $|V(G)|$ and $|E(G)|$ from the user.
# 2.) Ask the user for the incidence matrix of $G$.
# 3.) Asks the user for the value of $m$.
# 4.) For each edge, $e = v_i v_j$ with $i < j$ the user indicates with a $0$ 
#     that $\sigma_{i,j} will be fixed as the identity permutation for all 
#     full $m$-fold covers that the program considers, or the user 
#     indicates with a $1$ that $\sigma_{i,j}$ is not fixed. 
#
#   PROCESS
#     The program counts the number of proper $\mathcal{H}$-colorings of $G$ 
#     for each full $m$-fold cover, $\mathcal{H}$ of $G$, satisfying: 
#     for any edge $v_i v_j$ with $i < j$ that received a 0 in the 4th step, 
#     $\mathcal{H}$ has $\sigma_{i,j}$ as the identity permutation.
#     Thus if $q$ is the number of 1's entered by the user,
#     the program considers $(m!)^q$ full $m$-fold covers of $G$.
#
#   OUTPUT
#     The first output will be the maximum number of proper colorings 
#     over all $m$-fold covers that the program considers.
#
#     The second output will be the minimum number of proper colorings 
#     over all $m$-fold covers that the program considers.
# 
# To verify Theorem 3 for $m = 2,3,4,5$ use the following inputs:
# 1.) Enter the number of vertices: 4
#     Enter the number of edges: 6
#
# 2.) Enter the incidence matrix(one row at a time and space-seperated values)
#           E1 E2 E3 E4 E5 E6
#       V1: 1 1 1 0 0 0
#       V2: 1 0 0 1 1 0
#       V3: 0 1 0 1 0 1
#       V4: 0 0 1 0 1 1
#
#
#
# 3.) Enter the fold number: m
#
# 4.) Enter the edges that will correspond to the identity permuation in the cover 
#     ('0' for identity, '1' otherwise)::
#       E1: 0
#       E2: 0
#       E3: 0
#       E4: 1
#       E5: 1
#       E6: 1
#
#   OUTPUTS FOR EACH VALUE OF $m$ 
#       When $m = 2$:
#       2
#       0
#
#       When $m = 3$:
#       12
#       0
#
#       When $m = 4$:
#       60
#       24
#
#       When $m = 5$:
#       182
#       120
#
#
#################

import math as math
import itertools as iter
from tqdm import tqdm


#
# Creation of the incidence matrix of $G$. Returns a 2D Matrix.
# When $G$ has $l$ vertices and $w$ edges, the user specifies $l$ and $w$
# and then the incidence matrix.
# 
# 
def incidenceM_Creation(l, w):
    # Initialize the incidence matrix with zeros
    matrix = [[0] * w] * l

    print("Enter the incidence matrix(one row at a time and space-seperated values):")
    for cols in range(w):
        if (cols == 0):
            print(f"    E{cols + 1}", end=" ")
        else:
            print(f"E{cols + 1}", end=" ")
    for i in range(l):
        print()
        row = input(f"V{i + 1}: ").strip().split()
        if len(row) != w:
            print("Error: Number of elements in the row does not match the number of columns.")
            incidenceM_Creation(l, w)
        matrix[i] = [int(val) for val in row]
    print()   
    return matrix

# 
# Returns a 1D Matrix
# 
# For each edge, $e = v_i v_j$ with $i < j$ the user indicates with a $0$ 
#     that $\sigma_{i,j} will be fixed as the identity permutation for all 
#     full $m$-fold covers that the program considers, or the user 
#     indicates with a $1$ that $\sigma_{i,j}$ is not fixed.
# 
# 
#
def edgeID_Creation(w):
    matrix = []
    print(f"\nEnter the edges that will correspond to the identity permuation in the cover ('0' for identity, '1' otherwise): ")
    for i in range(w):
        matrix.append(int(input(f"Edge {i + 1}: ")))
        print()
    return matrix

#
# Generates every possible coloring based on the second coordinates of 
# the elements of $L(v)$ for each $v \in V(G)$.
#
def generate_colorings(n, length):
    return [list(perm) for perm in iter.product(range(1, n + 1), repeat=length)]

#
# Determines whether a coloring is proper.
#
def coloring_function(m, v, e, incidence_matrix, p_edges, colorings):
    c = 0
    for i in range(m**v):
        z = 0
        for j in range(e):
            a = -1
            b = -1
            for k in range(v):
                if (incidence_matrix[k][j] == 1):
                    a = b
                    b = k
            if (p_edges[j][colorings[i][a] - 1] != colorings[i][b]):
                z += 1
        if (z == e):
            c += 1
    return c

##### DRIVER PROGRAM ######

# Ask $|V(G)|$ and $|E(G)|$ from the user.
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

# Ask the user for the incidence matrix of $G$.
incidence_matrix = incidenceM_Creation(v, e)

# Ask the user for the value of $m$.
m = int(input("\nEnter the fold number: "))


# Generates every possible coloring based on the second coordinates of 
# the elements of $L(v)$ for each $v \in V(G)$.
colorings = generate_colorings(m, v)

# D is the maximum number of proper colorings 
# over all $m$-fold covers that the program considers.

# d is the minimum number of proper colorings 
# over all $m$-fold covers that the program considers.
D = 0
d = (m**v)

# Generates all permutations of $[m]$.
permutations = list(iter.permutations(range(1, m + 1)))


# Enter the edges that will correspond to the identity permuation 
# in the cover ('0' for identity, '1' otherwise):
edges_id = edgeID_Creation(e)

# Determine the number of 1's entered by the user.
q = 0 
for i in range(e):
    q += edges_id[i]

# Generates all full $m$-fold covers that the program will consider.
covers = generate_colorings(math.factorial(m), q)

#
# Counts the number of proper $\mathcal{H}$-colorings of $G$ 
# for each full $m$-fold cover, $\mathcal{H}$ of $G$, satisfying: 
# for any edge $v_i v_j$ with $i < j$ that received a 0, 
# $\mathcal{H}$ has $\sigma_{i,j}$ as the identity permutation.
# Thus if $q$ is the number of 1's entered by the user,
# the program considers $(m!)^q$ full $m$-fold covers of $G$. 
#
p = [[0] * m] * e
for i in tqdm (range(math.factorial(m)**q), desc="Calculating..."):
    for j in range(e):
        count = 0
        if edges_id[j]== 1:
            p[j] = permutations[covers[i][count] - 1]
            count += 1
        else:
            p[j] = permutations[0]
    c = coloring_function(m, v, e, incidence_matrix, p, colorings)
    if c > D:
        D = c
    if c < d:
        d = c

# OUTPUTS
print(f'Max: {D}')
print(f'Min: {d}')