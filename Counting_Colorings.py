#################
#
#
# 
# This program is to show that Theorem 3 of 
# "On Polynomial Representations of Dual DP Color Functions" by Jeffrey A. Mudrock
# is true.
#
# Department of Mathematics and Statistics, University of South Alabama, Mobile, AL 36688. 
# E-mail: mudrock@southalabama.edu
#
#
# We assume for this program that $G = K_4$.
#
#
# Incidence matrix for a $K_4$:
# V1: 1 1 1 0 0 0
# V2: 1 0 0 1 1 0
# V3: 0 1 0 1 0 1
# V4: 0 0 1 0 1 1
#
# E1: 0
# E2: 0
# E3: 0
# E4: 1
# E5: 1
# E6: 1
#
#################

import math as math
import itertools as iter
from tqdm import tqdm

# 
# params (num_rows, num_cols)
# Creation of the incidence matrix. Returns a 2D Matrix
# 
# 
def incidenceM_Creation(num_rows, num_cols):
    # Initialize the incidence matrix with zeros
    matrix = [[0] * num_cols] * num_rows

    print("Enter the incidence matrix(one row at a time and space-seperated values):")
    for cols in range(num_cols):
        if (cols == 0):
            print(f"    E{cols + 1}", end=" ")
        else:
            print(f"E{cols + 1}", end=" ")
    for i in range(num_rows):
        print()
        row = input(f"V{i + 1}: ").strip().split()
        if len(row) != num_cols:
            print("Error: Number of elements in the row does not match the number of columns.")
            return None
        matrix[i] = [int(val) for val in row]
    print()   
    return matrix


# 
# params (num_rows)
# Asks the user what edges they want to keep. Returns a 1D Matrix
#
# It is sufficient to check all covers for $sigma_1,2 1,3 1,4$ by [17]
#
def edgeID_Creation(num_rows):
    matrix = []
    print(f"\nEnter the edges you want to keep('1' to keep, '0' for identity): ")
    for i in range(num_rows):
        matrix.append(int(input(f"Edge {i + 1}: ")))
        print()
    return matrix


#
# params (n, length)
# 
#
def generate_permutations(n, length):
    return [list(perm) for perm in iter.product(range(1, n + 1), repeat=length)]


#
# params (m, num_vertices, num_edges, incidence_matrix, p_edges, colorings)
# 
# 
# 
# TODO: Explain c is mathcal u
#
# 
#
def coloring_function(m, num_vertices, num_edges, incidence_matrix, p_edges, colorings):
    c = 0
    for i in range(m**num_vertices):
        z = 0
        for j in range(num_edges):
            a = -1
            b = -1
            for k in range(num_vertices):
                if (incidence_matrix[k][j] == 1):
                    a = b
                    b = k
            if (p_edges[j][colorings[i][a] - 1] != colorings[i][b]):
                z += 1
        if (z == num_edges):
            c += 1
    return c

#### DRIVER #####

# Ask |V(G)| and |E(G)| from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Ask the user for each $v \in V(G)$ which $e \in E(G)$ they have. 
incidence_matrix = incidenceM_Creation(num_vertices, num_edges)
#print(incidence_matrix)

# Asks the user for the m-fold cover of G.
m = int(input("\nEnter the fold number: "))

#p_edges = array2D_Creation(num_edges, m, "edge permutation")
#print(p_edges)


# Generates every possible coloring permutation
colorings = generate_permutations(m, num_vertices)
#print(colorings)

# D = $P_{DP}^*(G,m)$ which is the maximum number of colorings over all m-fold covers
# d = $P_{DP}^*(G,m)$ which is the minumum number of colorings over all m-fold covers
D = 0
d = (m**num_vertices)

# 
permutations = list(iter.permutations(range(1, m + 1)))
#print(permutations)

# Asks the user which edges take on the identity permutation
edges_id = edgeID_Creation(num_edges)
edges_sum = 0 
#print(edges_id)
for i in range(num_edges):
    edges_sum += edges_id[i]


L = generate_permutations(math.factorial(m), edges_sum)
#print(L)

#
#  
#
#
p = [[0] * m] * num_edges
for i in tqdm (range(math.factorial(m)**edges_sum), desc="Calculating..."):
    for j in range(num_edges):
        count = 0
        if edges_id[j]== 1:
            p[j] = permutations[L[i][count] - 1]
            count += 1
        else:
            p[j] = permutations[0]
    c = coloring_function(m, num_vertices, num_edges, incidence_matrix, p, colorings)
    if c > D:
        D = c
    if c < d:
        d = c
print(f'Max: {D}')
print(f'Min: {d}')